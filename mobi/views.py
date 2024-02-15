from django.shortcuts import render

from home.models import A_category, B_category, Bayt_parse


# Create your views here.
def homeviewmobile(request):
    context = {
        'a_cat_list': A_category.objects.all()
    }

    return render(request, 'mobile-index.html', context)


def category_detailsmobile(request, id):
    context = {
        'b_cat_list': B_category.objects.filter(a_category_id=id)
    }

    return render(request, 'mobile-category_det.html', context)


def single(request, bcat_id, id):
    context = {
        'data1': Bayt_parse.objects.filter(b_category_id=id)
    }
    print('test')
    return render(request, 'singlemobile.html', context)
