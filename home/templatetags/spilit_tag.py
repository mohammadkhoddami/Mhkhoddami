from django import template

register = template.Library()

@register.filter
def work_spiliter(value, delimiter=","):
    return value.split(delimiter)