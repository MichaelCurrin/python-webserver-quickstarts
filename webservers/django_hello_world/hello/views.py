from django.shortcuts import render

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent("""\
            <html>
            <head>
                <title>Hello World!</title>
            </head>
            <body>
                <h1>Hello world</h1>
                <p>Hello, world! Hola Mundo!</p>
            </body>
            </html>
        """)
        return HttpResponse(response_text)
