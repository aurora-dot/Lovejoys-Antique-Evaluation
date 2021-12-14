from django.shortcuts import redirect, render
from .forms import EvaluationForm


# Create your views here.
def index(request):
    return render(request, "app/index.html")


def request_evaluation(request):
    if request.user.is_authenticated:
        form = EvaluationForm(request.POST)
        if form.is_valid():
            print()
        return render(request, "app/request_evaluation.html", {"form": form})
    else:
        return redirect("/")
