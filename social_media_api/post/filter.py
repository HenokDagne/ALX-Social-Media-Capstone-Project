import django_filters
from post.models import Post 

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Partial match, case-insensitive
    user_email = django_filters.CharFilter(field_name='user__email', lookup_expr='iexact')  # Exact match

    class Meta:
        model = Post
        fields = ['title', 'user_email']

        

 