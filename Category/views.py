from django.shortcuts import render, get_object_or_404
from content_module.models import content, category
# Create your views here.


def sport(request):
    sport_content = content.objects.filter(category_id=1)
    return render(request, "Category/sport.html", {
        'sport_content': sport_content
    })


def action(request):
    sport_content = content.objects.filter(category_id=2)
    return render(request, "Category/sport.html", {
        'sport_content': sport_content
    })


def scary(request):
    sport_content = content.objects.filter(category_id=3)
    return render(request, "Category/sport.html", {
        'sport_content': sport_content
    })

