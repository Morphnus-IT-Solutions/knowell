from django import template

from web.models import Banner

register = template.Library()

def render_logo(request):
    logo = Banner.objects.filter(type='logo').exclude(image=None)
    if logo:
        logo = logo[0]
    return dict(request=request, logo=logo)
register.inclusion_tag('web/logo.html')(render_logo)


def render_footer(request):
    return dict(request=request)
register.inclusion_tag('web/footer.html')(render_footer)
