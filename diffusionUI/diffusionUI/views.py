from django.shortcuts import render
from django.http import HttpResponseRedirect
from .pipeline import DiffusionModel

def index(request):
    context = {}
    return render(request, "diffusionUI/index.html", context)

def generate_image(request):
    if request.method == "POST":
        positive_prompt = request.POST.get("positive_prompt")
        model = DiffusionModel()
        image = model.generate_image(positive_prompt)

    return HttpResponseRedirect("/")
