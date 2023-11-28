from django.shortcuts import render, redirect

# páginas de error

def my_404_view(request, exception):
    return render (request, '404.html', status=404)

def my_500_view(request):
    return render (request, '500.html', status=500)


def fake_admin(request):
    if request.method == 'GET':
        return render(request, 'f_login.html')
    return redirect('index')