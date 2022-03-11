from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from .forms import CaptchaForm


def home(request):

    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            messages.success(request, "Formulário enviado com sucesso!")
        else:
            messages.error(request,"Confirme que não é robô!")
    form = CaptchaForm()
    context = {
        'form':form
    }

    return render(request, 'home.html',context)