from django.shortcuts import render
from django.http import HttpResponse
from models import Article
# Create your views here.

def Home(request):
    return HttpResponse("<h1>hello django!</h1>")

def Another_page(request):
    return HttpResponse("<h1>That is another page</b></h1>")
def detail(request,my_args):
    print type(my_args)
    return HttpResponse("<b>you 're looking at my_args %s.</b>"%(int(my_args)+5))
def detail_db(req,my_args):
    post = Article.objects.all()[int(my_args)]
    str =("title =%s,catagory=%s,date_time=%s,content =%s" %(post.title,post.category,post.date_time,post.content))
    return HttpResponse(str)