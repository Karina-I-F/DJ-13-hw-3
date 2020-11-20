from django import template

register = template.Library()


@register.filter()
def get_color(value):
    if value == '-' or 0 < float(value) < 1.0:
        return 'White'
    elif 1.0 <= float(value) < 2.0:
        return 'LightPink'
    elif 2.0 <= float(value) < 5.0:
        return 'LightCoral'
    elif float(value) >= 5.0:
        return 'Red'
    elif float(value) < 0:
        return 'DarkGreen'
