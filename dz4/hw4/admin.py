from django.contrib import admin
from hw4.models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'date','updated', 'user',)
    search_field = ['author', 'date', 'updated', 'user',]

    

