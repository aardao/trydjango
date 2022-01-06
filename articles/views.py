from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib.auth.decorators import login_required

from articles.models import Article
from .forms import ArticleForm

def article_search_view(request):
    print('article_search_view')
    #print(request.GET)  
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

# @login_required
# def article_create_view(request):
#     #esto crea un formulario vacio siempre
#     print('article_create_view parte1')
#     form2 = ArticleForm()
#     print('parte1')
#     context={
#         "form": form2
#     }
#     if request.method=="POST":
#         #si el metodo es post, el formulario viene relleno
#         print('article_create_view parte2')
#         form=ArticleForm(request.POST)
#         context['form']=form
#         if form.is_valid():
#             print('article_create_view parte3')
#             title=form.cleaned_data.get("title")
#             content=form.cleaned_data.get("content")
#             print(title,content)
#             article_object = Article.objects.create(title=title, content=content)
#             context['object']=article_object
#             context['created']=True
#     return render(request,"articles/create.html",context)


@login_required
def article_create_view(request): 
    form = ArticleForm(request.POST or None)
    context={
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form']= ArticleForm()
        #una forma de redirect
        return redirect(article_object.get_absolute_url())
        #otra forma de redirect
        #return redirect('article-detail',slug=article_object.slug)
    return render(request,"articles/create.html",context)


def article_detail_view(request,slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": article_obj,
    }

    return render(request,"articles/detail.html",context)