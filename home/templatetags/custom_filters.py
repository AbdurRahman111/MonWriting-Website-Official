from django import template

register = template.Library()

@register.filter
def starts_with(value, arg):
    """Check if a string starts with a specific substring."""
    if str(value)[0:8] == 'https://':
        return True
    return False
