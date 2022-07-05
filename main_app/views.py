from django.shortcuts import render
from django.http import HttpResponse

# classes
class Cat: 
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
        
# dummy data
cats = [
    Cat('Lolo', 'tabby', 'foul little demon', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]

# Create your views here.
def home(request):
    return render(request, 'main_app/home.html')

def about(request):
    return render(request, 'main_app/about.html')

def cats_index(request):
    return render(request, 'main_app/cats/index.html', {'cats': cats})