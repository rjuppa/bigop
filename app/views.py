from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView, FormView
from app.tasks import test1
from datetime import datetime


class HomeView(TemplateView):
    template_name = "page.html"

    def get_context_data(self, **kwargs):
        kwargs['time'] = datetime.now()
        return kwargs

    def post(self, request, *args, **kwargs):

        test1.delay('This is just a test.')
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)
