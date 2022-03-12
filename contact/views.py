import urllib
import json
import requests
from urllib import response
from urllib.request import Request, urlopen
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm


def contact(request):
 
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():          

            return HttpResponse('data submitted successfully')

        else:
            
            """ Begin reCaptcha Validation """
            recaptchaResponse = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            print("Valor",recaptchaResponse)
            values = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptchaResponse
            }
            resp = requests.post(url, data=values)
            # data = urllib.parse.urlencode(values)
            # req = urllib.request.Request(url, data)
            # response = urlopen(req)
            result = resp.json()

            if not result['success']:
                messages.error(request,"reCAPTCHA inválido!")

            context = {
                'form': form
            }
            return render(request,'home2.html', context)
    else:
        form = PostForm()
        context = {
                'form': form
            }
        return render(request,'home2.html', context)