# pylint: disable=no-member

from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect

from portal.models import Product, Category, ProductAnswer, ProductQuestion
from portal.forms import AnswerQuestionForm, ProductForm, ProductQuestionForm
# Create your views here.


def home(request):
    return render(request, 'portal/home.html', {})


def my_products(request):
    products = Product.objects.filter(
        user=request.user)

    context = {
        'products': products
    }

    return render(request, 'portal/my_products.html', context)


def product_new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product()
            product.user = request.user
            product.name = form.cleaned_data['name']
#            product.slug = slugify(form.cleaned_data['name'])
            product.quantity = form.cleaned_data['quantity']
            product.price = form.cleaned_data['price']
            product.short_description = form.cleaned_data['short_description']
            product.description = form.cleaned_data['description']
            product.status = 'Active'
            product.save()

            if categories := Category.objects.filter(id__in=request.POST.getlist('categories')):
                for category in categories:
                    product.categories.add(category)

            return redirect('my_products')

    form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'portal/product_new.html', context)


def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if product.user != request.user:
        return HttpResponseForbidden

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.quantity = form.cleaned_data['quantity']
            product.price = form.cleaned_data['price']
            product.short_description = form.cleaned_data['short_description']
            product.description = form.cleaned_data['description']
            product.categories = form.cleaned_data['categories']
            product.status = form.cleaned_data['status']

            product.save()
            return redirect('my_products')

    form = ProductForm(instance=product)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'portal/product_edit.html', context)


def product_show(request, slug):
    product = get_object_or_404(Product, slug=slug, status='Active')
    questions = ProductQuestion.objects.filter(
        product=product, status='Active')
    form = ProductQuestionForm()

    context = {
        'form': form,
        'product': product,
        'questions': questions
    }

    return render(request, 'portal/product_show.html', context)


def product_new_question(request, product_id):
    product = get_object_or_404(Product, id=product_id, status='Active')

    if request.method == 'POST':
        form = ProductQuestionForm(request.POST)
        if form.is_valid():
            question = ProductQuestion()
            question.user = request.user
            question.product = product
            question.question = form.cleaned_data['question']
            question.status = 'Active'
            question.save()

    return redirect('product_show', product.slug)


def product_images(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
 #   images = ProductImages.objects.filter(product=product)

    context = {
        'product': product,
        'images': {}
    }

    return render(request, 'portal/product_images.html', context)


def product_question(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'portal/product_question.html', context)


def product_answer_question(request, product_id, question_id):
    product = get_object_or_404(Product, pk=product_id)
    question = get_object_or_404(ProductQuestion, pk=question_id)

    form = AnswerQuestionForm()

    if request.method == 'POST':
        form = AnswerQuestionForm(request.POST)
        if form.is_valid():
            product_answer = ProductAnswer()
            product_answer.user = request.user
            product_answer.answer = form.cleaned_data['answer']
            product_answer.product_question = question
            product_answer.status = 'Active'
            product_answer.save()

            return redirect('product_question', product.id)

    context = {
        'form': form,
        'product': product,
        'question': question
    }

    return render(request, 'portal/product_answer_question.html', context)
