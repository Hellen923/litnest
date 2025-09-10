from django.shortcuts import render, get_object_or_404
from .models import Novel
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    genre_filter = request.GET.get('genre')
    novels = Novel.objects.all().order_by('-created_at')

    if query:
        novels = novels.filter(Q(title__icontains=query) | Q(author__icontains=query))
    if genre_filter and genre_filter != "All":
        novels = novels.filter(genre__iexact=genre_filter)

    genres = Novel.objects.values_list('genre', flat=True).distinct()
    return render(request, 'novels/home.html', {'novels': novels, 'genres': genres})

def novel_detail(request, novel_id):
    novel = get_object_or_404(Novel, id=novel_id)
    return render(request, 'novels/detail.html', {'novel': novel})
