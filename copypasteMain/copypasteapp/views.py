from django.shortcuts import render

# Create your views here.

default_data = ''


def index(re):
    if re.method == 'POST':
        data = re.POST['text_Area']
        fun(data)
        global default_data
        default_data = data
        return render(re, 'index.html', {'data': data})

    else:

        return render(re, 'index.html', {'data': default_data})


def fun(data):
    with open('file.txt', 'w') as file:
        file.write(data)