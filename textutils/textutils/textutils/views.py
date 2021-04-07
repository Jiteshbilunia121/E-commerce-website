# i have created this File .
import string
import re
from django.http import HttpResponse
from django.shortcuts import render  
def index(request):   
    return render(request,'index.html') 

def analyze(request):
    djtext = request.POST.get('text','default') 
    removepunc = request.POST.get('removepunc','off')
    removelines = request.POST.get('removelines','off')
    removespaces = request.POST.get('removespaces','off')
    
    Word = djtext
    if removepunc == 'on':
        newstring = ""
        punc = string.punctuation;
        for char in djtext:
            if char not in punc:
                newstring = newstring + char
        djtext = newstring
        
    if removelines == 'on':
        newstring=""    
        for char in djtext:
            if char != '\n' and char != '\r':  
                newstring = newstring + char
        djtext = newstring
        
    if removespaces == 'on':
        newstring = ""    
        for index,char in enumerate(djtext):
            if(not(djtext[index] == " " and djtext[1+index] == " ")):
                newstring = newstring + char  
        djtext = newstring
    params = {'word':Word , 'newword':djtext}    
    return render(request, 'punctuationremove.html',params)
    
        
    
     
#def capital(request):
 #   return HttpResponse("Capiatalize first letter")
#def newlineremove(request):
#    return HttpResponse("removing new lines")
#def spaceremove(request): 
 #   return HttpResponse("removing spaces ")
#def charcount(request):
 #   return HttpResponse("Character counting")