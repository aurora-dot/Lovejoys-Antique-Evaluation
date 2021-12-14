from django.http import Http404
from django.shortcuts import redirect, render
from .forms import EvaluationForm
from accounts.models import User


# Create your views here.
def index(request):
    return render(request, "app/index.html")


def request_evaluation(request):
    if request.user.is_authenticated:
        submitted = False
        form = EvaluationForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
            submitted = True
        return render(
            request,
            "app/request_evaluation.html",
            {"form": form, "submitted": submitted},
        )
    else:
        return redirect("/")


def admin_view_requests(request):
    if (
        request.user.is_authenticated
        and request.user.is_staff
        or request.user.is_superuser
    ):
        user_requests = User.objects.prefetch_related("evaluation_requests").all()
        return render(
            request, "app/admin_view_requests.html", {"user_requests": user_requests}
        )
    else:
        raise Http404
