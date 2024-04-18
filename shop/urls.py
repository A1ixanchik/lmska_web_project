from django.urls import path

from shop.views import greetings, cats, list_item, detail_item

urlpatterns = [
    path('greetings/', greetings),
    path('facts/', cats),
    path('', list_item),
    path('<int:pk>/', detail_item)
]

