from django.conf.urls import url
from catalog import views
urlpatterns = [
    url(r'^api/catalog',views.catalog_list),
    url(r'^api/catalog/(?P<pk>[0-9]+)$',views.catalog_detail),
]
