from django.template.defaulttags import register

@register.filter
def lookup(object, key):
    if hasattr(object, key):
        return getattr(object, key)
    
    return None


@register.filter
def get_type(value):
    if value.__class__.__name__ == "ManyRelatedManager":
        return "list"
    else:
        return "str"
