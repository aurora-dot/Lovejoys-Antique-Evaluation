from django.conf import settings
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

# Create your views here.


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():

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
                },
            )
            send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            return render(request, "accounts/success_signup.html")
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


def validate_email(request, uidb64, token):
    return_title = "Invalid."
    return_text = "The activation link is invalid."

    User = get_user_model()

    try:
        user = User.objects.get(pk=urlsafe_base64_decode(uidb64))
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if not user.is_active:
            user.is_active = True
            user.save()
            return_title = "Success"
            return_text = (
                "Thank you for your email confirmation. Now you can login your account."
            )

    return render(
        request, "accounts/validate.html", {"title": return_title, "text": return_text}
    )
