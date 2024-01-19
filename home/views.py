from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, "home/index.html")


def aboutPage(request):
    return render(request, "home/index.html")


def contactPage(request):
    return render(request, "home/index.html")