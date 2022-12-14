from django import forms
from portal.models import Product, ProductAnswer, UserProfile
from django.contrib.auth.models import User

from s3direct.widgets import S3DirectWidget


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('slug', 'user',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': "Nome",
            'categories': "Categories",
            'quantity': "Quantidade",
            'price': "Preço",
            'short_description': "Descrição curta",
            'description': "Descrição",
        }


class ProductQuestionForm(forms.Form):
    question = forms.CharField(
        label='Perguntar',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 'id': 'question', 'placeholder': 'Faça sua pergunta!'
            }
        ),
        required=True
    )


class AnswerQuestionForm(forms.ModelForm):
    class Meta:
        model = ProductAnswer
        exclude = ('user', 'product_question', 'status')

        widgets = {
            'answer': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'answer',
                'placeholder': 'Responda aqui...'
            }),
        }

        labels = {
            'answer': "Resposta"
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'remote_customer_id')

        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'cpf': "CPF",
            'address': "Endereço",
            'number': "Número",
            'address2': "Complemento",
            'city': "Cidade",
            'district': "Bairro",
            'state': "Estado",
            'country': "País",
            'zipcode': "CEP",
            'phone': "Telefone",
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'first_name': "Nome",
            'last_name': "Sobrenome",
        }

class S3DirectUploadForm(forms.Form):
    images = forms.URLField(widget=S3DirectWidget(dest='product_images'))
