from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=122, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your name'}))
    subject = forms.CharField(max_length=122, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your subject'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Enter your email'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Enter your message'}))
