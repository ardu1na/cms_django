from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

from prensa.models import Articulo, Tag, Categoria
"""

## TODO:
## achicador y renombrador de imagenes
## test import-export
# create groups 4 prensa
# add meta admin and change admin url


DEPLOY NGNX ----¿ +GNUNICORN ? media?

## TODO NEXT FASE:
# create special endpoints for gral querys
# add swagger docs
# do fe with react
# modulo mercado local

"""




###########################################################################
################ pagina de INICIO

def index(request):
    last_three_articles = Articulo.objects.filter(publicado=True).order_by('-fecha')[:3]
    template_name = 'page/index.html'
    context = {
        'articles' : last_three_articles,

    }
    return render (request, template_name, context)

###########################################################################









###########################################################################
################ PRENSA APP

def articulo(request, slug):
    articulo = Articulo.objects.filter(slug=slug, publicado=True).last()
    template_name = 'page/prensa/articulo.html'
    last_six_articles =  Articulo.objects.filter(publicado=True).order_by('-fecha').exclude(slug=articulo.slug)[:7]
    context = {
        'articles' : last_six_articles,
        'object': articulo,

    }
    return render (request, template_name, context)

def prensa(request):
    articulos_list = Articulo.objects.filter(publicado=True)
    query = request.GET.get('q')

    if query:
        articulos_list = articulos_list.filter(
            Q(titulo__icontains=query) |
            Q(texto__icontains=query)
        )

    paginator = Paginator(articulos_list, 1) 
    page = request.GET.get('page')
    articulos = paginator.get_page(page)

    last_articles =  Articulo.objects.filter(publicado=True).order_by('-fecha')[:10]
    last_destacados = Articulo.objects.filter(publicado=True, destacado=True).order_by('-fecha')[:4]

    tags = Tag.objects.all()[:15]
    categorias = Categoria.objects.all()[:10]

    template_name = 'page/prensa/prensa.html'
    context = {
        'destacados': last_destacados,
        'last' : last_articles,
        'articulos': articulos,
        'tags': tags,
        'categorias': categorias,

    }
    return render (request, template_name, context)

def categorias(request, slug):
    categoria = Categoria.objects.filter(slug=slug).last()
    articulos_list = Articulo.objects.filter(publicado=True, categoria=categoria)
    paginator = Paginator(articulos_list, 4) 
    page = request.GET.get('page')
    articulos = paginator.get_page(page)

    last_articles =  Articulo.objects.filter(publicado=True).order_by('-fecha')[:10]

    tags = Tag.objects.all()[:15]
    categorias = Categoria.objects.exclude(id=categoria.id)[:10]

    template_name = 'page/prensa/query.html'
    context = {
        'last' : last_articles,
        'articulos': articulos,
        'tags': tags,
        'categorias': categorias,
        'categoria':categoria,

    }
    return render (request, template_name, context)

def tags(request, slug):
    tag = Tag.objects.filter(slug=slug).last()
    articulos_list = Articulo.objects.filter(publicado=True, tags=tag)
    paginator = Paginator(articulos_list, 4) 
    page = request.GET.get('page')
    articulos = paginator.get_page(page)

    last_articles =  Articulo.objects.filter(publicado=True).order_by('-fecha')[:10]

    tags = Tag.objects.exclude(id=tag.id)[:15]
    categorias = Categoria.objects.all()[:10]

    template_name = 'page/prensa/query.html'
    context = {
        'last' : last_articles,
        'articulos': articulos,
        'tags': tags,
        'categorias': categorias,
        'tag':tag,

    }
    return render (request, template_name, context)

################ END PRENSA
###########################################################################


