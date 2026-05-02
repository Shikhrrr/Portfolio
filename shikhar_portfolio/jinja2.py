"""
Jinja2 environment configuration for Django.
Exposes static, url, and other helpers to all Jinja2 templates.
"""

from jinja2 import Environment
from django.templatetags.static import static
from django.urls import reverse
from django.utils.safestring import mark_safe


def environment(**options):
    """Create and configure the Jinja2 environment."""
    env = Environment(**options)

    def _csrf_input(request):
        """Render a CSRF hidden input for use in Jinja2 templates."""
        from django.middleware.csrf import get_token
        token = get_token(request)
        return mark_safe(
            f'<input type="hidden" name="csrfmiddlewaretoken" value="{token}">'
        )

    env.globals.update({
        'static': static,
        'url': reverse,
        'csrf_input': _csrf_input,
    })
    return env
