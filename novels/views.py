from django.shortcuts import render, get_object_or_404, redirect
from .models import Novel, Bookmark, ReadingProgress
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def landing(request):
    return render(request, 'novels/landing.html')

def novels_home(request):
    query = request.GET.get('q')
    genre_filter = request.GET.get('genre')
    novels = Novel.objects.all().order_by('-created_at')

    if query:
        novels = novels.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(summary__icontains=query))
    if genre_filter and genre_filter != "All":
        novels = novels.filter(genre__iexact=genre_filter)

    genres = Novel.objects.values_list('genre', flat=True).distinct()
    return render(request, 'novels/home.html', {'novels': novels, 'genres': genres})

def novel_detail(request, novel_id):
    novel = get_object_or_404(Novel, id=novel_id)
    is_bookmarked = False
    if request.user.is_authenticated:
        is_bookmarked = Bookmark.objects.filter(user=request.user, novel=novel).exists()
    return render(request, 'novels/detail.html', {'novel': novel, 'is_bookmarked': is_bookmarked})

@login_required
def toggle_bookmark(request, novel_id):
    novel = get_object_or_404(Novel, id=novel_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, novel=novel)
    if not created:
        bookmark.delete()
        messages.success(request, f"Removed {novel.title} from bookmarks.")
    else:
        messages.success(request, f"Added {novel.title} to bookmarks.")
    return redirect('novel_detail', novel_id=novel_id)

@login_required
def update_progress(request, novel_id):
    if request.method == 'POST':
        progress = float(request.POST.get('progress', 0))
        novel = get_object_or_404(Novel, id=novel_id)
        reading_progress, created = ReadingProgress.objects.get_or_create(user=request.user, novel=novel)
        reading_progress.progress = progress
        reading_progress.save()
        return redirect('novel_detail', novel_id=novel_id)
    return redirect('novels_home')
