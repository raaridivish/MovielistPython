from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {'movie_list': movie}
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})
    # return HttpResponse('This is movie no %s' % movie_id)


def add_movie(request):
    if request.method == "POST":
        movie_name = request.POST.get('movie_name')
        movie_desc = request.POST.get('movie_desc')
        movie_year = request.POST.get('movie_year')
        movie_img = request.FILES['movie_img']

        movie = Movie(name=movie_name, desc=movie_desc, year=movie_year, img=movie_img)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    if request.method == "POST":
        movie_name = request.POST.get('movie_name')
        movie_desc = request.POST.get('movie_desc')
        movie_year = request.POST.get('movie_year')
        movie_img = request.FILES['movie_img']
        movie = Movie.objects.get(id=id)
        form = MovieForm(request.POST or None, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'edit.html', {'form': form, 'movie': movie})
    else:
        movie = Movie.objects.get(id=id)
        form = MovieForm(request.POST or None, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html', {'movie': movie})
