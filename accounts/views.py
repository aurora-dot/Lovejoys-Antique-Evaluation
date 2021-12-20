import requests
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import OTPForm, UserCreationForm
from .models import User
from .tokens import account_activation_token

# Create your views here.


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    form = UserCreationForm(request.POST or None)
    if settings.USE_HEROKU:
        data = {"form": form, "site_key": settings.HCAPTCHA_TOKEN}
    else:
        data = {"form": form}

    if request.method == "POST":
        if form.is_valid():
            if not check_hcaptcha(request):
                return redirect("accounts:signup")
            user = form.save(commit=False)
            user.is_active = False
            email = user.email
            user.save()

            mail_subject = "Activate your account."
            message = render_to_string(
                "accounts/validate_email.html",
                {
                    "user": user,
                    "domain": get_current_site(request).domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                    "protocol": "https" if request.is_secure() else "http",
                },
            )
            send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [email])

            return render(request, "accounts/success_signup.html")

    return render(request, "accounts/signup.html", data)


def validate_email(request, uidb64, token):
    return_title = "Invalid."
    return_text = "The activation link is invalid."

    try:
        user = User.objects.get(pk=urlsafe_base64_decode(uidb64))
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if (
        user is not None
        and account_activation_token.check_token(user, token)
        and not user.is_active
    ):
        user.is_active = True
        user.save()
        return_title = "Success"
        return_text = (
            "Thank you for your email confirmation. Now you can login your account."
        )

    return render(
        request, "accounts/validate.html", {"title": return_title, "text": return_text}
    )


def login_view(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()

        if settings.USE_HEROKU:
            data = {"form": form, "site_key": settings.HCAPTCHA_TOKEN}
        else:
            data = {"form": form}

        if request.method == "POST":
            if not check_hcaptcha(request):
                return redirect("accounts:login")
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session["pk"] = user.pk
                user.otp.save()
                return redirect("verify/")

        return render(request, "accounts/login.html", data)
    else:
        return redirect("app:index")


def verify_view(request):
    if request.session.get("pk") and not request.user.is_authenticated:
        form = OTPForm(request.POST or None)
        pk = request.session.get("pk")

        if pk:
            try:
                user = User.objects.get(pk=pk)
            except User.DoesNotExist:
                return Http404

            pin = user.otp.pin

            if not request.POST:
                mail_subject = "Lovejoy Antiques: OTP"
                message = render_to_string("accounts/otp_email.html", {"pin": pin})
                send_mail(
                    mail_subject, message, settings.DEFAULT_FROM_EMAIL, [user.email]
                )

            if form.is_valid():
                pin_input = form.cleaned_data.get("pin")
                if pin_input == pin:
                    login(request, user)
                    return redirect("app:index")

        return render(request, "accounts/otp.html", {"form": form})
    else:
        if request.user.is_authenticated:
            return redirect("app:index")
        else:
            return redirect("accounts:login")


def check_hcaptcha(request):
    if settings.USE_HEROKU:
        captcha_response = request.POST.get("h-captcha-response")
        data = {
            "secret": settings.HCAPTCHA_SECRET_KEY,
            "response": captcha_response,
        }
        r = requests.post(settings.HCAPTCHA_VERIFY_URL, data=data)
        result = r.json()
        return result["success"]
    else:
        return True
