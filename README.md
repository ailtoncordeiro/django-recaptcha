

# Formulário de contato em Django com reCAPTCHA

Formulário feito com o framework Python Django com o uso do reCAPTCHA visando o bloqueio de bots.


| Desenvolvedor       |  GitHub             |
| ------------------- | ------------------- |
|  Ailton Cordeiro    |  @ailtoncordeiro    |



### Repositório de desenvolvimento!

disponível em: https://github.com/ailtoncordeiro/django-recaptcha.git



**Linguagens utilizadas no desenvolvimento:**

<p align="left"> <a href="#" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a> Python </p>

<p align="left"> <a href="#" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="python" width="40" height="40"/></a> Django (Framework) </p>

<p align="left"> <a href="#" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" alt="python" width="40" height="40"/></a> HTML5 </p>

<p align="left"> <a href="#" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="python" width="40" height="40"/></a> CSS3</p>

<p align="left"> <a href="#" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="python" width="40" height="40"/></a> JS </p>



### Requisitos para utilizar o projeto:

1. Python 3.8
2. Django 4.0.3



### Como executar:

Acessar o https://www.google.com/recaptcha/about/ e criar as chaves públicas e privadas e adicionar no arquivo settings.py que está localizado no diretório recaptcha.

```bash
RECAPTCHA_PUBLIC_KEY = 'public_key_here'
RECAPTCHA_PRIVATE_KEY = 'private_key_here'
```
Após a geração das chaves é necessário ter no ambiente que irá executar o aplicativo pelo menos a versão 3.8 do Python e o instalador de pacotes Python PIP

Após já ter instalado o Python 3.8 e o PIP

instalar (**de preferência em uma virtual env**) os pacotes necessários contido no arquivo requeriments.txt

```bash
pip install -r requeriments.txt
```

Realizar o makemigrations para preparação do código SQL para criação das tabelas no banco de dados.
```bash
python manage.py makemigrations
```

Executar a criação das tabelas no banco de dados.
```bash
python manage.py migrate
```

Criar o usuário inicial (superuser).
```bash
python manage.py createsuperuser
```

Por fim executar o servidor próprio
```bash
python manage.py runserver
```


