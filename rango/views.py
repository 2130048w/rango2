# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page

def index(request):
    # query the database for a list of ALL categories currently stored
    # order the categories by no. likes in descending order
    # retrieve the top 5 only - or all less than 5
    # place the list in our context_dict dictionary
    # that will be passed to the template engine
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    #Render the response and send it back
    return render(request,'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "Carla Whiteford"}
    return render(request,'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict={}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)