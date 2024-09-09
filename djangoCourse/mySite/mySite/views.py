from string import punctuation

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home <a href='/'>back</a>")

# def removepunc(request):
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("Remove Punc")
#
# def capfirst(request):
#     return HttpResponse("Capitalize First")
#
# def about(request):
#     return HttpResponse("About")
#
# def newlineremove(request):
#     return HttpResponse("newline remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("char count")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('allcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    analyzed = ""
    work = ""
    if removepunc == 'on':
        punctuations = '''.,'"?!{}[]()-:;/`'''
        for a in djtext:
            if a not in punctuations:
                analyzed += a
        work += "Removed Punctuations "
    if fullcaps=='on' :
        work += "UPPERCASE "
        if analyzed =="":
            analyzed = djtext.upper()
        else:
            analyzed = analyzed.upper()

    if newlineremover=='on' :
        work += "New Line Removed "
        if analyzed == "":
            for a in djtext:
                if a != '\n' and a!='\r':
                    analyzed += a
        else:
            temp = ""
            for a in analyzed:
                if a != '\n' and a!='\r':
                    temp += a
            analyzed = temp

    if spaceremover=='on' :
        work += "Space Removed "
        if analyzed == "":
            for a in djtext:
                if a != ' ':
                    analyzed += a
        else:
            temp = ""
            for a in analyzed:
                if a != ' ':
                    temp += a
            analyzed = temp

    if charcount == 'on':
        analyzed += "\nThe Charcater Count of the input is " + str(len(djtext))
        work += "Length of Input "

    if analyzed=="":
        analyzed = djtext
    parms = {'purpose':work,'analyzed_text':analyzed}
    return render(request,'analyze.html',parms)