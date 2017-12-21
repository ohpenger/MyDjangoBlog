from django import template
from ..models import Post,Category
from django.utils.html import format_html
register=template.Library()
@register.simple_tag
def get_recent_post(num=5):
    return Post.objects.all()[:num]
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')
@register.simple_tag
def get_categorys():
    return Category.objects.all()
@register.simple_tag
def circle_page(current_page,loop_page):
    offset=abs(current_page-loop_page)
    if offset<3 or (loop_page-current_page)<=5:
        page_ele='<a href="?page=%s">%s</a>'%(loop_page,loop_page)
        return format_html(page_ele)
    else:
        return ""