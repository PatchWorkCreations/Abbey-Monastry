from django import template

register = template.Library()

@register.filter
def format_post(value):
    # Perform any formatting or manipulation of the post content here
    # For example, split the post content into lines and add line breaks
    lines = value.split('\n')
    formatted_post = '<br>'.join(lines)
    return formatted_post