from django.contrib import admin
from .models import Family

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
        list_display = (
                'kakao',
                'state',
                'address',
                'gmoney',
                'kmoney',
                'country',    
                'gphoto',
                'tphoto',
                'detail',
                'writepw',
        )

class Photo(admin.ModelAdmin):
    class Media:
        js = ('jquery.js', 'inlines.js',)
