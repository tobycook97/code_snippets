from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST': #Post is a type of Http request. (GET is anoter one)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # cleaned datat is styuff which has been converted to pyhton types from the form input :) 
            messages.success(request, f'Account created for {username}!') #we add one of these messages and it prints in blog base.html
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,"users/register.html", {'form':form})


#different types of messages:

#messages.debug
#messages.info
#messages.successs
#messages.warning
#messages.error
