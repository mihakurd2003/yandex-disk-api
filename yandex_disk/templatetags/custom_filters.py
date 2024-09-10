from django import template

register = template.Library()

@register.filter
def file_extension(filename):
    return filename.split('.')[-1].lower()