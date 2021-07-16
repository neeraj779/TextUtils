# This file is created by me - Neeraj
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyzer(request):
    djtext = request.POST.get('text', 'default')
    on_off_punc = request.POST.get('removepunc', 'off')
    on_off_upper = request.POST.get('upper', 'off')
    on_off_char = request.POST.get('char_counter', 'off')

    if on_off_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if on_off_upper == 'on':
        analyzed = djtext.upper()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if on_off_char == 'on':
        count = 0
        for i in djtext:
            count += 1
        analyzed = f"{djtext} : character count is {count}"
        params = {'purpose': 'Character counts', 'analyzed_text': analyzed}

    if (on_off_char == "off", on_off_punc == "off", on_off_upper == "off"):
        return HttpResponse("Plese select on off the operation and try again")

    return render(request, 'analyze.html', params)
