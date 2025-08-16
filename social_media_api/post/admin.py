from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'user', 'content', 'create_at', 'updated_at', 'image')
	list_editable = ('title', 'content', 'image')
	readonly_fields = ('create_at', 'updated_at')
	search_fields = ('title', 'user__username')
