"""
To render html web pages
"""

from django.http  import HttpResponse

HTML_STRING = """
<h1>Hellow World</h1>
"""

def home_view(request):
    return HttpResponse(HTML_STRING)