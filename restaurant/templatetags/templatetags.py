from django import template
register = template.Library()

@register.simple_tag
def define(val=None):
  return val


@register.simple_tag
def vales(key,dictt):
    return dictt[key]