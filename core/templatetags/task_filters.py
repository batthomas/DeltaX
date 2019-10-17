from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="addclass")
def add_class(field, css):
    old_css = field.field.widget.attrs.get("class", None)
    if old_css:
        css = old_css + css
    return field.as_widget(attrs={"class": css})


@register.filter(name="upto")
@stringfilter
def upto(value, delimiter=" "):
    return value.split(delimiter)[0]