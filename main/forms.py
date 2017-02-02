# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:12:10 2017

@author: gaurav
"""

from django import forms


class DocumentForm(forms.Form):
   
    docfile = forms.FileField(
        label = 'Select a file',
        help_text = 'max. 42 megabytes')                       #data from the above form would be accessible as request.FILES['file'].
    
    