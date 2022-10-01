from django import forms
from portal.models import Product, ProductAnswer


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