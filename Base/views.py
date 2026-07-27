from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
# Create your views here.

def home(request):
    return render(request, 'home.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        contact = request.POST.get('number')
        print(name, email, content, contact)

        if len(name)>2 and len(name)<30 :
            pass
        else:
            messages.error(request, 'Name must be between 2 and 30 characters')
            return render(request, 'home.html')
        
        if len(email)>5 and len(email)<25 :
            pass
        else:
            messages.error(request, 'Email must be between 5 and 25 characters')
            return render(request, 'home.html')
        
        if len(contact)>10 and len(contact)<15 :
            pass
        else:
            messages.error(request, 'Contact number must be between 10 and 15 characters')
            return render(request, 'home.html')
        
        ins=models.Contact(name=name, email=email, content=content, number=contact)
        ins.save()
        messages.success(request, 'Your message has been sent successfully!')
        print('Data has been saved to the database')
        print('the request is no pass')
    
    return render(request, 'home.html')