from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm, NewMovieForm

def title(request):
    allMovies = Movie.objects.all
    return render(request, 'list.html', {'all': allMovies})

def add(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('bluRayInfo:add')
    else:
        form = MovieForm()
    allMovies = Movie.objects.all
    return render(request, 'list.html', {'form': form, 'all': allMovies})

def edit(request):
    if request.method == "POST":
        movieID = request.POST.get('editMovie')
        movie = get_object_or_404(Movie, id = movieID)
        form = NewMovieForm(request.POST, request.FILES, instance = movie)
        if form.is_valid():
            form.save()
            return redirect('bluRayInfo:add')
    else:
        form = NewMovieForm(instance = movie)
    all_movies = Movie.objects.all()
    return render(request, 'list.html', {'form': form, 'all': all_movies})
    
def delete(request, item_id):
    try:
        form = Movie.objects.get(id=item_id)
        form.delete()
    except Movie.DoesNotExist:
        pass
    allMovies = Movie.objects.all
    return render(request, 'list.html', {'all': allMovies})

def searchMovies(request):
    search = request.GET.get('search', '')
    if search:
        searchedMovies = Movie.objects.filter(description__icontains = search)
    else:
        searchedMovies = Movie.objects.all()
    return render(request, 'list.html', {'all': searchedMovies})

def sortMovies(request):
    sortedAlpha = Movie.objects.order_by('name')
    return render(request, 'list.html', {'all': sortedAlpha})

def sortID(request):
    sortedID = Movie.objects.order_by('id')
    return render(request, 'list.html', {'all': sortedID})
