from django.shortcuts import render
from django.contrib import messages
from .models import Background
from .forms import TestimonialForm


def background_info(request):
    
    if request.method == "POST":
        testimonial_form = TestimonialForm(data=request.POST)
        if testimonial_form.is_valid():
            testimonial_form.save()
            messages.add_message(request, messages.SUCCESS, "Testimonial received! Thank you for your feedback")

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