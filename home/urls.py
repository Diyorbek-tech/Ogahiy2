from django.urls import path
from .views import *


urlpatterns = [
    path('', homeview, name='homeview'),
    path('<int:id>/', category_details, name='category_details'),
    path('<int:bcat_id>/<int:id>/', single, name='single'),
]
