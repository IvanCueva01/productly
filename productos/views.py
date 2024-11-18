from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
from .models import Producto
# Create your views here.

# /productos


def index(request):
    productos = Producto.objects.all()
    # productos = Producto.objects.filter(puntaje__gte=4.5)
    # productos = Producto.objects.get(pk=1)
    # print(productos)
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    return render(
        request,
        'detalle.html',
        context={'producto': producto}
    )


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )
