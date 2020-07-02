from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzer = ""
        for char in djtext:
            if char not in punctuations:
                analyzer = analyzer + char
        params = {'purpose': 'Removed Punctuations', 'Analyzed': analyzer}
        djtext = analyzer

    if capitalize == "on":
        analyzer = ""
        for char in djtext:
            analyzer = analyzer + char.upper()
        params = {'purpose': 'Capitalize Punctuations', 'Analyzed': analyzer}
        djtext = analyzer


    if (extraspaceremover == "on"):
        analyzer = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzer= analyzer + char

        params = {'purpose': 'Removed NewLines', 'Analyzed': analyzer}
        # Analyze the text
        djtext = analyzer


    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'Analyzed': analyzed}
        # Analyze the text

    if removepunc != "on" and capitalize != "on" and newlineremover != "on" and extraspaceremover != "on":
        return HttpResponse('Error')
    return render(request, 'analyzer.html', params)



