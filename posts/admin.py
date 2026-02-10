from django.contrib import admin

# Register your models here.
from .models import Category,Post,Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')  
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at')
    list_filter = ('status', 'category', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}  
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('status', 'created_at')    


admin.site.register(Comment)
