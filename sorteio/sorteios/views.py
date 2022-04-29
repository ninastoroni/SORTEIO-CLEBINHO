from django.shortcuts import render
from django.http import HttpResponse

list = []

def index(request):
    return render(request,'index.html')

def adicionar(request):

    if request.method == "POST":


        nome = request.POST['nome']
        list.append(nome)
        combobox = request.POST['qtdgrupos']

        print(nome)
        print(list)
        print(combobox)


    return render(request, 'index.html')


