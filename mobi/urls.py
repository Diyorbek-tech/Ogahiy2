from django.urls import path
from .views import *

urlpatterns = [
    path('', homeviewmobile, name='homeviewm'),
    path('<int:id>/', category_detailsmobile, name='category_detailsm'),
    path('<int:bcat_id>/<int:id>/', single, name='singlemobile'),
]
