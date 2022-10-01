# pylint: disable=invalid-str-returned,too-few-public-methods

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('Category', null=True, blank=True,
                               related_name='cat_child', on_delete=models.CASCADE)
    order = models.IntegerField(null=True, blank=True)
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        Category, blank=True, related_name="categories")
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    short_description = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Inactive")

    @property
    def questions_no_answer(self):
        return self.productquestion_set.filter(status='Active', productanswer__isnull=True)  # pylint: disable=no-member

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            super(Product, self).save()
         #   self.slug = '%s-%i' % (slugify(self.name), self.id)
            self.slug = f"{slugify(self.name)}-{self.id}"  # pylint: disable=no-member
        super(Product, self).save(*args, **kwargs)


class ProductQuestion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    question = models.TextField()
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Inactive")

    @property
    def get_answers(self):
        return self.productanswer_set.filter()  # pylint: disable=no-member

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self) -> str:
        return self.question


class ProductAnswer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product_question = models.ForeignKey(
        ProductQuestion, on_delete=models.CASCADE)
    answer = models.TextField()
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Inactive")

    class Meta:
        verbose_name_plural = "Answers"

    def __str__(self) -> str:
        return self.answer
