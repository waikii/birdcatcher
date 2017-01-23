from django import template
register = template.Library()

@register.filter

# Is passed a list and returns the ith element of that list

def index(List, i):
    return List[int(i)]