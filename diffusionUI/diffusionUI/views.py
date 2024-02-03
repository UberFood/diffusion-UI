from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "diffusionUI/index.html", context)
