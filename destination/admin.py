from django.contrib import admin
from .models import Mf_result, Places,Place_rating,Destimages,Hotel,Comment

class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['name']

class mfadmin(admin.ModelAdmin):
    search_fields = ['place__name', 'user__username']

admin.site.register(Places,PlaceAdmin)
admin.site.register(Place_rating)
admin.site.register(Destimages)
admin.site.register(Hotel)
admin.site.register(Comment)
admin.site.register(Mf_result,mfadmin)


