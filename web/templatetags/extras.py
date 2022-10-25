from django import template

register = template.Library()


@register.filter(name='filtering')
def filter_by(obj, filter_by):
  return obj.order_by(filter_by)
