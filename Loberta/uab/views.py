from django.shortcuts import render
from .models import URLs

from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def index(request):
    url_list = URLs.objects.all()
    context = {'url_list': url_list}
    return render(request, 'url-list.html', context)
# Create your views here.
