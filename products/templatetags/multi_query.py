from django import template



register = template.Library()


@register.simple_tag(takes_context=True)
def add_to_current_url(context,**kwargs):
    current_url = context['request'].GET.copy()
    for k, v in kwargs.items():
        current_url[k] = v
    for k in [k for k, v in current_url.items() if not v]:
        del current_url[k]
    return current_url.urlencode()



