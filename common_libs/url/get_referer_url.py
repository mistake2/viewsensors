from django.utils.http import is_safe_url, urlunquote
from urllib.parse import urlparse


def get_referer_url(request):
    url = request.META.get('HTTP_REFERER')
    if url:
        url = urlunquote(url)
    if not is_safe_url(url = url, host = request.get_host()):
        url = '/'

    return urlparse(url).path