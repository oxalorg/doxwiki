from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models
from . import marker

# Create your views here.
def about(req):
    return HttpResponse('This is doxwiki')


def index(req):
    sort_by = req.GET.get('sort', '-date_created')
    pages = models.Page.objects.order_by(sort_by).all()
    context = {'pages': pages}
    return render(req, 'doxwiki/index.html', context)


def page(req, slug):
    page = models.Page.objects.get(slug=slug)
    if not page:
        # prompt to create a page
        pass
    context = {'page': page}
    return render(req, 'doxwiki/page.html', context)


def tag(req, slug):
    tag = get_object_or_404(models.Tag, name=slug)
    context = {'tag': tag}
    return render(req, 'doxwiki/tag.html', context)


def category(req, slug):
    category = get_object_or_404(models.Category, name=slug)
    context = {'category': category}
    return render(req, 'doxwiki/category.html', context)


class TagList(generic.ListView):
    model = models.Tag
    context_object_name = 'tags'


class CategoryList(generic.ListView):
    model = models.Category
    context_object_name = 'categories'


def attachment(req, slug, attachment):
    return HttpResponse('attachment')
