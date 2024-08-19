from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def add_class(field, css_class):
    """
    Adds a CSS class to a form field.
    """
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={'class': css_class})
    return field  # Return the original field if it doesn't have 'as_widget'

@register.filter
def linebreaks(value):
    """Convert newlines to <p> tags."""
    value = value.replace('\r\n', '\n')  # Normalize line endings
    paragraphs = value.split('\n\n')  # Split by double newlines
    # Use mark_safe to ensure that the HTML is not auto-escaped
    return mark_safe('<p>{}</p>'.format('</p><p>'.join(paragraphs)))
