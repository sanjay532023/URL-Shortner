from django.shortcuts import render, redirect
from .models import short_urls
from .forms import UrlForm
from .shortner import shortner
from django.http import HttpResponse
import win32console

def Home(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def details(request):
    # if request.method == 'POST':
    obj = short_urls.objects.all()
    return render(request, 'detail.html', {'short': obj})


def display_long_url(request):
    if request.method == 'POST':
        name = request.POST['shoturl']
        obj = short_urls.objects.filter(short_url=name)
        return render(request, 'display_long_url.html', {'data': obj})


## deleting Values
def delete_shorted_url(request):
    if request.method == 'POST':
        name = request.POST['del_shorted_url']
        obj = short_urls.objects.get(short_url=name)
        obj.delete()
        if obj:
            message = name + '  Deleted Succesfuly!'
            return render(request, 'delete_shorted_url.html', {'message': message})

        else:
            message = "Error Please enter Valid Short Name "
            return render(request, 'delete_shorted_url.html', {'message': message})


def Make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortner().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"

    return render(request, 'home.html', {'form': form, 'a': a})


