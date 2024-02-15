from django.shortcuts import render
from .models import A_category, B_category, Bayt_parse


# Create your views here.

def homeview(request):
    context = {
        'a_cat_list': A_category.objects.all()
    }

    return render(request, 'sayt-index.html', context)


def category_details(request, id):
    context = {
        'b_cat_list': B_category.objects.filter(a_category_id=id)
    }

    return render(request, 'category_details.html', context)


def single(request, bcat_id, id):
    context = {
        'data': Bayt_parse.objects.filter(b_category_id=id)
    }
    return render(request, 'single.html', context)
