from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from  . import models
from django.shortcuts import get_object_or_404


#book_list
def books_list(request):
    if request.method == "GET":
        query = models.Books.objects.all().order_by('-id')
        context_object_name = {
            'book_list': query,
        }
        return render(request, template_name = 'book.html',
                      context= context_object_name)

def books_detail(request, id):
    if request.method == "GET":
        query = get_object_or_404(models.Books, id=id)
        context_object_name = {
            'books_list_id': query,
        }
        return render(request,
                      template_name = 'book_detail.html',
                      context= context_object_name)


def emodji (request):
    if request.method == 'GET':
        return  HttpResponse('🥶')

def text (request):
    if request.method == 'GET':
        return  HttpResponse('Hello World')

def image (request):
    if request.method == 'GET':
        return  HttpResponse('<img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRLM_YMOn41npXKC5fX-TSRfe20jO-nK1cfON36eskj5100UzlH4JMmJVsjNYxZPV4R0vw6DHIw0dqN-osUB5Iw7Q" alt="cat gif" />')

def about_me(request):
    if request.method == 'GET':
        return  HttpResponse('My name is Ilgiz and I am a student at Geeks ')
def text_and_photo(request):
    if request.method == 'GET':
        return  HttpResponse('<img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRLM_YMOn41npXKC5fX-TSRfe20jO-nK1cfON36eskj5100UzlH4JMmJVsjNYxZPV4R0vw6DHIw0dqN-osUB5Iw7Q" alt="cat gif" />Hello World')

def system_time (datetime):
    if system_time(datetime):
        return datetime