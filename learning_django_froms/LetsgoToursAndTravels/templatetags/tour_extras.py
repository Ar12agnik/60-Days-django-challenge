from django import template
from ..models import Tour,pictures as picture 
register = template.Library()
@register.simple_tag
def total_tours():
    return Tour.objects.count()
@register.inclusion_tag('latest_tours.html')
def show_latest_tours():
    latest_tours=Tour.objects.order_by('-created_at')
    return {'tours':latest_tours}
@register.inclusion_tag('pictures.html')
def show_pictures(name=None):
    if name is not None:
        pictures=picture.objects.filter(tour=name)
        if pictures:
            return {'pictures':pictures}
        else:
            return {"tour":name}