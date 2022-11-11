from django import template
from datetime import timedelta

register = template.Library()


@register.filter
def to_str(value):
    s = str(value)
    return s[0:4]

# register.filter('to_str', to_str)