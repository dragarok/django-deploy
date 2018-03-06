from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):

    '''
    This cuts out all values of arg from string
    '''
    return value.replace(arg, '')

# register the custom filter to template library

# register.filter('cut',cut)
# This was removed by using decorator on line 6