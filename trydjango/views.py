"""
To render html web pages
"""

from django.http  import HttpResponse


from articles.models import Article

def home_view(request):
    name = "Justin"

    article_obj = Article.objects.get(id=2)
   

    HTML_STRING = f"""
    <h1>{article_obj.title}  ({article_obj.id})!</h1>
    <p>{article_obj.content}!</p>
    """

   
    return HttpResponse(HTML_STRING)