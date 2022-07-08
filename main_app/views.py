from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Dog, Toy
from .forms import FeedingForm

class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/dogs/'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'
    
class ToyList(ListView):
  model = Toy
  template_name = 'main_app/toys/index.html'

class ToyDetail(DetailView):
  model = Toy
  template_name = 'main_app/toys/detail.html'

class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

# Create your views here.
def home(request):
    return render(request, 'main_app/home.html')

def about(request):
    return render(request, 'main_app/about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'main_app/dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    feeding_form = FeedingForm()
    toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
    return render(request, 'main_app/dogs/detail.html', {'dog': dog, 'feeding_form': feeding_form, 'toys':toys_dog_doesnt_have})

def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)

def assoc_toy(request, dog_id, toy_id):
  Dog.objects.get(id=dog_id).toys.add(toy_id)
  return redirect('detail', dog_id=dog_id)