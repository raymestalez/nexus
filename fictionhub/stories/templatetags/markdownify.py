from django import template
import markdown
import bleach
 
register = template.Library()
 
@register.filter
def markdownify(text):
    html = markdown.markdown(text)

    linkify_html = bleach.linkify(html)
    tags = ['img', 'p', 'em', 'strong'] # bleach.ALLOWED_TAGS
    attributes = {
        '*': ['class', 'style'],
        'A': ['href', 'rel'],
        'img': ['src', 'alt', 'style'],
    }
    styles = ['float','font-weight', 'width']
    
    clean_html = bleach.clean(linkify_html, styles=styles, tags=tags, attributes=attributes, strip=True)
    return clean_html
