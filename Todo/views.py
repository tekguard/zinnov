from django.shortcuts import render
from.forms import ContactForm

def showPage(request):
    f = ContactForm()
    return render(request,'contact.html',{'form':f})
def handleForm(request):
    if request.method=='POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            data = f.cleaned_data
            return render(request,'showData.html',data)
        else:
            return render(request,'contact.html',{'form':f})