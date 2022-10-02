from django.apps import AppConfig
import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex


class PortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portal'

    def ready(self):
        product = self.get_model('Product')
        algoliasearch.register(product, ProductIndex)


class ProductIndex(AlgoliaIndex):
    fields = ('id', 'name', 'short_description',
              'description', 'slug', 'price')
    settings = {'searchableAttributes': ['name', 'description']}
    index_name = 'product_index'
