from django import template
import textwrap

register = template.Library()


@register.filter(name='split')


def split(value):
    return '\n'.join(textwrap.fill(line,100) for line in value.split('\n'))


#return textwrap.fill(value)
