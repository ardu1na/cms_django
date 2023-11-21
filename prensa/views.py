from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

from prensa.models import Articulo, Tag
"""

## TODO:
## achicador y renombrador de imagenes
# 


# more security resources: https://djangopackages.org/grids/g/security/


# al crear la app al crear al usuario
 para Prensa ponerlo en grupo Prensa para otorgarle sus permisos y ponerlo como staff para que pueda acceder al panel



DEPLOY NGNX ----¿ +GNUNICORN ? media?

## TODO NEXT FASE:
# create special endpoints for gral querys
# do fe with react

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

    
    articulo_anterior = Articulo.objects.filter(publicado=True, fecha__lt=articulo.fecha).order_by('-fecha').first()
    if articulo_anterior:
        anterior = articulo_anterior.slug
    else:
        anterior = None
    articulo_siguiente = Articulo.objects.filter(publicado=True, fecha__gt=articulo.fecha).order_by('fecha').first()
    if articulo_siguiente:
        siguiente = articulo_siguiente.slug
    else:
        siguiente = None
    tags = Tag.objects.all()[:15]

    context = {
        'articles' : last_six_articles,
        'object': articulo,
        'anterior': anterior,
        'siguiente': siguiente,
        'tags': tags,

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

    paginator = Paginator(articulos_list, 4) 
    page = request.GET.get('page')
    articulos = paginator.get_page(page)

    last_articles =  Articulo.objects.filter(publicado=True).order_by('-fecha')[:10]
    last_destacados = Articulo.objects.filter(publicado=True, destacado=True).order_by('-fecha')[:4]

    tags = Tag.objects.all()[:15]

    template_name = 'page/prensa/prensa.html'
    context = {
        'destacados': last_destacados,
        'last' : last_articles,
        'articulos': articulos,
        'tags': tags,

    }
    return render (request, template_name, context)


def tags(request, slug):
    tag = Tag.objects.filter(slug=slug).last()
    articulos_list = Articulo.objects.filter(publicado=True, tags=tag)
    paginator = Paginator(articulos_list, 2) 
    page = request.GET.get('page')
    articulos = paginator.get_page(page)

    last_articles =  Articulo.objects.filter(publicado=True).order_by('-fecha')[:10]

    tags = Tag.objects.exclude(id=tag.id)[:15]

    template_name = 'page/prensa/query.html'
    context = {
        'last' : last_articles,
        'articulos': articulos,
        'tags': tags,
        'tag':tag,

    }
    return render (request, template_name, context)

################ END PRENSA
###########################################################################


