from django.shortcuts import render
from django.http import HttpResponseRedirect
from io import BytesIO
import base64

from .pipeline import DiffusionModel

def index(request):
    context = {}
    if request.method == "POST":
        positive_prompt = request.POST.get("positive_prompt")
        negative_prompt = request.POST.get("negative_prompt")
        model = DiffusionModel()
        image = model.generate_image(positive_prompt, negative_prompt)

        buffer_png = BytesIO()
        image.save(buffer_png, format="PNG", kind='PNG')

        context = {
            'img_str': base64.b64encode(buffer_png.getvalue()).decode('utf-8'),
        }
    return render(request, "diffusionUI/index.html", context)
