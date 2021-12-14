from django.shortcuts import render

# from django.core.mail import send_mail


# Create your views here.
def index(request):
    # send_mail('subject', 'body of the message',
    # 'no-reply@lovejoyantiques.xyz', ['user@example.com'])
    return render(request, "app/index.html")
