from django import template

register = template.Library()

@register.filter
def highlight_year(value, year=1888):

    if value == year:
        return f"<span style='color: red; font-weight: bold;'>{value}</span>"
    return value
