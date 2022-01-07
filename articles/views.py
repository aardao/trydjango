from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib.auth.decorators import login_required

from articles.models import Article
from .forms import ArticleForm

def article_search_view(request):
    print('article_search_view')
    #print(request.GET)  
    query = request.GET.get('q')  
    qs = Article.objects.search(query=query)
    ##puedo hacer cosas más complejas
    #qs = Article.objects.filter(title__icontains='2').search(query=query)
    context = {
            "object_list" : qs
    }
    return render(request,"articles/search.html",context=context)




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