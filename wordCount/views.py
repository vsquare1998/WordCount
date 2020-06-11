from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['textarea']

    splitted_text = text.split()

    word_count = {}

    for word in splitted_text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return render(request, 'count.html',{'original':text,'text' : word_count.items()})

def about(request):
    return render(request, 'about.html')