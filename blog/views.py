from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def get_author(request):
    template = loader.get_template("master.html")
    return HttpResponse(template.render())




