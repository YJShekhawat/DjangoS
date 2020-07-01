from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("""<h1>Hello</h1> <a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-5"> Google</a>""")
# def about(request):
#     fp=open(r"C:\Users\VIJAY SINGH\PycharmProjects\DjangoS\dj1\dj1\1.txt","r")
#     a=fp.read()
#     return HttpResponse(a)
def index(request):
    params={"Name":"YJ","Place":"Jaipur"}
    return render(request,"index.html",params)

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc = request.GET.get('removepunch', 'off')
    Fullcaps=request.GET.get('fullcaps','off')
    extras=request.GET.get('spacer','off')
    newline = request.GET.get('newline', 'off')
    count=0
    if removepunc=="on":
        count=count+1
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char


        params={"purpose":"Punctuations Removed","analyzed_text":analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if(Fullcaps=="on"):
        cap=djtext.upper()
        count = count + 1
        params = {"purpose": "Capitalized Successfully", "analyzed_text": cap}
        djtext = cap
        # return render(request, 'analyze.html', params)

    if(newline=="on"):
        x=""
        count = count + 1
        for text in djtext:
            if text!='\n' and text!='\r':
                x=x+text
            else:
                x=x+" "
        params = {"purpose": "Newlines Removed", "analyzed_text": x}
        djtext = x
        # return render(request,'analyze.html',params)
    if(extras=="on"):
        r = ""
        count = count + 1
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                r=r+char

        params = {"purpose": "ExtraSpaces Removed", "analyzed_text": r}
        djtext=r

        # return render(request, 'analyze.html', params)
    # if(charcount=="on"):
    #     c=0
    #     for i in djtext:
    #         c=c+1
    #     x="no of counted characters = "
    #     x=x+str(c)
    #     params = {"purpose": "Counted Charaters", "analyzed_text": x}
    #     return render(request,'analyze.html',params)
    #
    #

    if count>=1:
        if count>=2:
            params={"purpose": "Operations Successful", "analyzed_text": djtext}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error You Don't Choose Any operation")
# def removepunch(request):
#     djtext=request.GET.get('text','default')
#     return HttpResponse(djtext)

# def capitalizef(request):
#     return HttpResponse("capitalizef")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>back </a>")
# def charcount(request):
#     return HttpResponse("charcount")
