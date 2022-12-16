from django import template
register = template.Library()
@register.filter
def subtract(value):
    return round(100 - value * 100)
