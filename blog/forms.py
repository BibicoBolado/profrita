from django import forms
from django.core.mail import send_mail
from django.conf import settings

class Contact(forms.Form):
    name =      forms.CharField(label='Nome',max_length=100,
    widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Digite o Nome Aqui'}))
    #required=false isso     serve para
    #dizer que o campo não é obrigatório
    email =     forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Digite o Email Aqui'}))
    message=    forms.CharField(
        label='Menssagem',widget=forms.Textarea(attrs={'class' : 'form-control','placeholder': 'Deixe o Recado Aqui'})
        )
    
    def sendMail(self,name,email,message):
        subject = 'Contato Blog %s' %name
        message = 'Nome: %s; Email: %s; Mensagem: %s' %(name,email,message)
        send_mail(subject,message,settings.EMAIL_HOST_USER ,[settings.CONTACT_EMAIL])