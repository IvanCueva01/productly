from django import template
register = template.Library()


@register.filter(name="add_attr")
def add_attr(field, css):
    attrs = {}
    definition = css.split(',')
    for d in definition:
        key, val = d.split(':')
        attrs[key] = val
    return field.as_widget(attrs=attrs)
