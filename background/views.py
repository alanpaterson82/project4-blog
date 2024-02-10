from django.shortcuts import render
from .models import Background
# Create your views here.


def background_info(request):
    """
    Renders the Background page
    """
    background = Background.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "background/background.html",
        {"background": background},
    )