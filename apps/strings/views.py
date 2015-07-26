# -*- coding: utf-8 -*-

import operator

from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import SearchForm


class HomeView(TemplateView, APIView):
    template_name = 'home.html'
    form_class = SearchForm

    def longest_substring(self, lines):
        """ Return longest substring for given lines
        that contained in minimum two lines. """
        longest = {}

        for line in lines:
            line_length = len(line)
            for i in range(line_length):
                for no in range(i + 1, line_length + 1):

                    substring = line[i:no].strip()
                    appears = sum(substring in line for line in lines)

                    # Add substring if it's appears more than one time and longer than one char.
                    if no - i > len(longest) and len(substring) > 1 and appears > 1:
                        if substring not in longest:
                            longest[substring] = appears
        if longest:
            return max(longest.iteritems(), key=operator.itemgetter(1))[0]
        return None

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = self.form_class()

        # If request is ajax return JSON.
        if self.request.is_ajax():
            lines = self.request.GET.get('query', '')
            if lines:
                substring = self.longest_substring(lines.split(','))
                return Response({'results': substring})

        return self.render_to_response(context)

