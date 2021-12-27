"""
To render html web pages
"""

from django.http  import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string



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

    HTML_STRING = render_to_string("home-view.html",context)

    # HTML_STRING = """
    # <h1>{title}  ({id})!</h1>
    # <p>{content}!</p>
    # """.format(**context)

   
    return HttpResponse(HTML_STRING)