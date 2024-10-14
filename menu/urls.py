from django.urls import path
from .views import item_list, item_list_serialized, item_detail

urlpatterns = [
    path("", item_list),
    path("drf/", item_list_serialized),
    path("<int:pk>/", item_detail),
]