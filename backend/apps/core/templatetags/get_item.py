from django import template

register = template.Library()

@register.filter
def get(dictionary, key):
    """
    Get a value from a dictionary by key.
    Usage: {{ mydict|get:key }}
    """
    if dictionary is None:
        return None
    return dictionary.get(key)
