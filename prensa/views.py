
from django.shortcuts import render
from prensa.models import Articulo


## TODO: ADD PAGINATION into main prensa page
## custom error pages
# !--crear prensa views y filters para categoria buscador y tags-->
## achicador y renombrador de imagenes

def index(request):
    last_three_articles = Articulo.objects.filter(publicado=True).order_by('-fecha')[:3]
    template_name = 'page/index.html'
    context = {
        'articles' : last_three_articles,

    }
    return render (request, template_name, context)


def articulo(request, slug):
    articulo = Articulo.objects.filter(slug=slug).last()
    template_name = 'page/prensa/articulo.html'
    last_six_articles =  Articulo.objects.filter(publicado=True).order_by('-fecha').exclude(slug=articulo.slug)[:7]
    context = {
        'articles' : last_six_articles,
        'object': articulo,

    }
    return render (request, template_name, context)