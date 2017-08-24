from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from ipware.ip import get_ip

from .models import Analytic
from .models import Url


class UrlForm(ModelForm):

    class Meta:
        model = Url
        fields = ['url']


def new_url(request):
    return render(request, 'new.html', {'url_form': UrlForm()})


def create_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save()
            return redirect('view_url', tiny_url=url.tiny_url)


def view_url(request, tiny_url):
    url_object = get_object_or_404(Url, tiny_url=tiny_url)
    url = request.build_absolute_uri(reverse('goto_url', args=(tiny_url,)))
    return render(request, 'show.html', {'url_object': url_object, 'url': url})


def goto_url(request, tiny_url):
    url_object = get_object_or_404(Url, tiny_url=tiny_url)
    url_object.clicks += 1
    url_object.save()

    analytic = Analytic(url=url_object, ip_address=get_ip(request), referrer=request.META['HTTP_REFERER'])
    analytic.save()
    return redirect(url_object.url)
