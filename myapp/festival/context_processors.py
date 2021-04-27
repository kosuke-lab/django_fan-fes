from .models import Area
from django.db.models import Count


def common(request):
    context = {
        'category_data'  : Area.objects.annotate(post_count=Count('festival')),
        'data' : Area.objects.all()
    }
    return context



