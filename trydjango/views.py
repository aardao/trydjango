"""
To render html web pages
"""

from django.http  import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string
from django.shortcuts import render



def home_view(request, *args, **kwargs):
    name = "Justin"

    print(args,kwargs)
 
    ramdom_id = random.randint(1,3)
    article_obj = Article.objects.get(id=ramdom_id)
    article_queryset = Article.objects.all()
   
    context = {
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
        "object_list": article_queryset
    }

    #otra forma de renderizar la plantilla pero sin mandar el request.
    #HTML_STRING = render_to_string("home-view.html",context)   
    #return HttpResponse(HTML_STRING)

    return render(request, "home-view.html", context)