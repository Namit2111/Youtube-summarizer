from django.shortcuts import render
from .utils import get_summary


# Create your views here.


def home(request):
    url = request.POST.get('url')
    try:
        if url:
            summary = get_summary(url)

        else:
            summary = ''
    except Exception as e:
        summary = 'Please enter a valid YouTube URL'
    return render(request, 'index.html', {'summary': summary})
