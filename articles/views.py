from django.shortcuts import render

from .models import Article

def article_search_view(request):
    print('article_search_view')
    print(request.GET)  
    query_dict = request.GET  # this is a dictionary
    
    try:
        query =int(query_dict.get("q"))    #<input type='text' name='q' />
    except: 
        query = None
    print('query: ' , query)
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
            "object" : article_obj
    }
    return render(request,"articles/search.html",context=context)


# Create your views here.
def article_detail_view(request,id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }

    return render(request,"articles/detail.html",context)