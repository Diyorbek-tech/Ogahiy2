from django.contrib import admin
from .models import *


@admin.register(Bayt_parse)
class ModelBaytparse(admin.ModelAdmin):
    list_display = ('word', 'mano', 'b_category')
    search_fields = ('word',)
    list_filter = ('b_category__name',)
    ordering = ('created',)


# Register your models here.
admin.site.register(A_category)
admin.site.register(B_category)
admin.site.register(Asarlar)
admin.site.register(Nasriy_bayon)
admin.site.register(N_kirib_kelgan)
admin.site.register(N_lugat)
