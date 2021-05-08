from django.contrib import admin
from .models import Home
from django.utils.html import format_html

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))
    
    readonly_fields=('created','updated')
    
    thumbnail.short_description = 'Image'
    
    list_display = ('id', 'thumbnail', 'title', 'created')
    list_display_links = ('id', 'thumbnail', 'title',) 
    search_fields = ('title',)
    list_filter = ('title',)

admin.site.register(Home, HomeAdmin)