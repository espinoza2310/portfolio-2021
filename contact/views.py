from django.shortcuts import render, redirect
from . forms import FormsContact
from django.core.mail import EmailMessage


# Create your views here.
def contact(request):
    forms_contact = FormsContact()

    if request.method == "POST":
        forms_contact = FormsContact(data=request.POST)
        if forms_contact.is_valid():
            name = request.POST.get("name") 
            email = request.POST.get("email") 
            message = request.POST.get("message") 

            email = EmailMessage("Messaje From Portfolio",
                                " User Name {} Email {} text to you: \n\n {}".format(name,email,message),"",["espinozatest2@gmail.com"])


            try:
                email.send()
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?Not-valid")




    return render(request, "contact/contact.html" ,{'myforms': forms_contact})
