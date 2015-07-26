# -*- coding: utf-8 -*-

from django import forms


class SearchForm(forms.Form):
    """
    Search substring form
    """
    search = forms.CharField(
        max_length=1204,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Type your strings...',
            'name': 'query',
        })
    )

