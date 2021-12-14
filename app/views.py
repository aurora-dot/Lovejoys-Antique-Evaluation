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
