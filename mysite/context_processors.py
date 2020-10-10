from django.db.models import Count, Q

from blog.models import Post, Category, Tag


def common(request):
    context = {
        'categories': Category.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'tags': Tag.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'latest': Post.objects.latest("created_at"),
    }
    return context