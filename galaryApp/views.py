from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Image
from .form import createForm

# Create your views here.


def main(request):
    images = Image.objects
    return render(request, 'main.html', {'images': images})


def createPage(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = createForm()
        return render(request, 'create.html', {"form": form})


def createFuction(request):
    images = Image()
    images.title = request.POST.get('title', False)
    images.description = request.POST.get('description', False)
    images.src = request.FILES.get('photo', False)
    images.save()
    messages.info(request, 'ADD')
    return redirect('mainPage')


def updatePage(request, update_id):
    update = get_object_or_404(Image, pk=update_id)
    form = createForm()
    return render(request, 'update.html', {'content': update, "form": form})


def updateFuction(request, update_id):
    update = get_object_or_404(Image, pk=update_id)
    if request.method == "POST":
        update.title = request.POST.get('title', False)
        update.description = request.POST.get('description', False)
        update.src = request.FILES.get('photo', False)
        update.save()
        messages.info(request, 'UPDATE')
        return redirect('mainPage')


def deleteFuction(request, delete_id):
    image = get_object_or_404(Image, pk=delete_id)
    if request.method == "GET":
        image.delete()
        messages.info(request, 'DELETE')
        return redirect('mainPage')
    else:
        pass
