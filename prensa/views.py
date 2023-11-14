
from django.shortcuts import render
from django.views.generic import DetailView
from prensa.models import Articulo


## TODO: ADD PAGINATION into main prensa page
## custom error pages



def index(request):
    last_three_articles = Articulo.objects.filter(publicado=True).order_by('-fecha')[:3]
    template_name = 'page/index.html'
    context = {
        'articles' : last_three_articles,

    }
    return render (request, template_name, context)



class ArticleDetail(DetailView):
    model = Articulo
    template_name = 'page/prensa/articulo.html' 