from django.shortcuts import render
from .models import Background
from .forms import TestimonialForm


def background_info(request):
    """
    Renders the Background page
    """
    background = Background.objects.all().order_by('-updated_on').first()
    testimonial_form = TestimonialForm()

    return render(
        request,
        "background/background.html",
        {
            "background": background,
            "testimonial_form": testimonial_form
        },
    )