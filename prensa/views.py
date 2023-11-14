from django.core.paginator import Paginator
from django.shortcuts import render
from prensa.models import Articulo, Tag, Categoria


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
    articulo = Articulo.objects.filter(slug=slug, publicado=True).last()
    template_name = 'page/prensa/articulo.html'
    last_six_articles =  Articulo.objects.filter(publicado=True).order_by('-fecha').exclude(slug=articulo.slug)[:7]
    context = {
        'articles' : last_six_articles,
        'object': articulo,

    }
    return render (request, template_name, context)


def prensa(request):
    if 'categoria' in request.GET:
        template_name = 'page/prensa/query.html'
        categoria_get = request.GET.get('categoria')
        categoria = Categoria.objects.filter(nombre=categoria_get).first()
        articulos_list = Articulo.objects.filter(publicado=True, categoria=categoria)
        paginator = Paginator(articulos_list, 2) 
        page = request.GET.get('page')
        articulos = paginator.get_page(page)

        context = {
            'articulos': articulos,
            'categoria': categoria,

        }
    else:
        articulos_list = Articulo.objects.filter(publicado=True)
        paginator = Paginator(articulos_list, 1) 
        page = request.GET.get('page')
        articulos = paginator.get_page(page)

        last_articles =  Articulo.objects.filter(publicado=True).order_by('-fecha')[:10]
        last_destacados = Articulo.objects.filter(publicado=True, destacado=True).order_by('-fecha')[:3]

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
## TODO: HACERLO CON PARAMS

