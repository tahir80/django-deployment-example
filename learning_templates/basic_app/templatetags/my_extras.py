from django import template

register = template.Library()


@register.filter('cut')
def cut(value, arg):
    """
     this cut out all values of "arg" from the string!

    """
    return value.replace(arg, '')


# register.filter('cut', cut)
