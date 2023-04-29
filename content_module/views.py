from django.shortcuts import render, get_object_or_404
from .models import content


# Create your views here.


def all_news_page(request):
    contents = content.objects.filter(is_active=True)
    return render(request, 'content_module/all_news_page.html', {
        "contents": contents
    })


def detail_news_page(request, slug):
    content_slug = get_object_or_404(content, slug=slug)
    return render(request, "content_module/detail_news_page.html", {
        'content': content_slug
    })


def latest_news(request):
    latest_content = content.objects.filter(rating__gt=69)
    return render(request, "content_module/latest_news.html", {
        'latest_content': latest_content
    })


def about_me(request):
    return render(request, 'content_module/about_me.html', {

    })
