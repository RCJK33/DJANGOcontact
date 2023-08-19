from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .form import ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string

# Create your views here.


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('Its valid')

            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # html = render_to_string(
            #     'emails/contactForm.html', {
            #         'name': name, 
            #         'email': email, 
            #         'message': message
            #         })

            # send_mail(name, message, email, ['to@email.com'], html_message=html)

            # sending email to Gmail
            send_mail(
                f"Contact Form Submission: {subject}",
                f"Name:  {name}\nEmail:  {email}\nMessage:  {message}.",
                email,
                ['rafa.11.rcj@gmail.com'],
                fail_silently=False,
            )

            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
