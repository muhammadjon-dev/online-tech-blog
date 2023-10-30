from django import template
from web_site.models import Category, Post
from django.db.models import Count

register = template.Library()


@register.simple_tag()
def get_category():
    category = Category.objects.all()
    return category[:7]

@register.simple_tag()
def get_posts_by_views():
    posts = Post.objects.annotate(cnt=Count("views")).order_by("-cnt")
    return posts[:3]