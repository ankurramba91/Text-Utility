

from django.http import HttpResponse
from django.shortcuts import render



def index(request):

    return render(request, 'index.html')


def analyze(request):
    #get the text
    djtext=request.POST.get('text', 'default')
    #Check Checkbox values
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charcount=request.POST.get('charcount', 'off')


    if removepunc == "on":
        puntuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for ch in djtext:
            if ch not in puntuations:
                analyzed=analyzed+ch
        params= {'purpose':'Remove Punctuations ','analyzed_text':analyzed}
        djtext = analyzed


    if(fullcaps=="on"):
        analyzed = ""
        for ch in djtext:
            analyzed=analyzed+ch.upper()
        params = {'purpose': 'Changed to Uppercase ', 'analyzed_text': analyzed}
        djtext=analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and  char!="\r":
                analyzed = analyzed + char


        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        djtext=analyzed
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, ch in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1] == " ") :
                analyzed = analyzed + ch
        params = {'purpose': 'Remove Extra Spaces ', 'analyzed_text': analyzed}
        djtext=analyzed
    if (charcount == "on"):
        analyzed = 1
        for index, ch in enumerate(djtext):
            if  ch>"a" and ch<"z" or ch>"A" and ch<"Z":
                analyzed = analyzed + 1
        params = {'purpose': 'Count Charater', 'analyzed_text': analyzed}
        djtext = analyzed
    if (removepunc != "on" and fullcaps!="on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on") :
        return  HttpResponse("Please Select any Thing")





    return render(request, 'analyze.html', params)
