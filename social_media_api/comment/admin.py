from django.contrib import admin
from comment.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'post', 'user', 'content', 'created_at')
	readonly_fields = ('created_at',)
	search_fields = ('content', 'user__username')


