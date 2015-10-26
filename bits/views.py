from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Bit

# Create your views here.

def index(request):
    latest_bits_list = Bit.objects.order_by('-bit_date')[:5]
    template = loader.get_template('bits/index.html')
    context = RequestContext(request, {
        'latest_bits_list': latest_bits_list,
    })
    return HttpResponse(template.render(context))
