from django import template
register = template.Library()
@register.filter
def prc(value):
    return  round(value * 100)