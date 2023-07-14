#I have created this file - Huzaim
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
#    return HttpResponse('''<h1>Hello</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k">CodewithHarry </a>''')

#def about(request):
#    return HttpResponse("About Huzaim")

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    #check if removepunc is checked or not
    removepunc = request.POST.get('removepunc', 'off')
    #check of uppercase is checked or not
    uppercase = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    #punctuations to check punctuations in text
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    #empty variable for converted text
    analyzed = ""

    if(removepunc=="on"): #if removepunc check is on
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        #variables to fulfil in html file
        params = {
            'purpose': 'Removed Punctuations',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        #analyze the text

    if(uppercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        # variables to fulfil in html file
        params = {
            'purpose': 'Changed in Upper Case',
            'analyzed_text': analyzed
        }
        # analyze the text
        djtext = analyzed

    #removes new lines
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char is not "\n" and char != "\r":
                analyzed = analyzed + char
        params = {
            'purpose': 'New Lines Removed',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {
            'purpose': 'Extra spaces Removed',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if(charcount == "on"):
        analyzed = ""
        analyzed = ('The number of characters are: '+str(len(djtext)))
        params = {
            'purpose': 'Character Counter',
            'analyzed_text': analyzed
        }
        djtext = analyzed
    if(removepunc!="on" and uppercase!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
# def capfirst(request):
#     return HttpResponse("Capfirst")
#
# def newlineremove(request):
#     return HttpResponse("NewLineRemove")
#
# def spaceremove(request):
#     return HttpResponse("Space Remover")
#
# def newlineremover(request):
#     return HttpResponse ("Capitalize first")
#
# def charcount(request):
#     return HttpResponse("charcouhnt")
