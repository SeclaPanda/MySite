from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime



def home(request):
    return  render(request, 'home.html')
    
def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html', context={
        'email': '123@123.ru',
        'phone': '+7 012 345 67 89',
        'time': datetime.now()
    })

def publications(request):
    return render(request, 'publications.html', context={
        'publications': [
            { 'name': 'One', 'date': '123'},
            { 'name': 'Two', 'date': '1234'}
        ]
    })

def publication(request):
    return render(request, 'publication.html') 

def css(request):
    return render(request, 'styles.css', content_type=css)