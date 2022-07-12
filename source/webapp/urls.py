from django.urls import path
from webapp.views import (main_view,
                          good_create_view,
                          good_view_)

urlpatterns = [
    path('', main_view, name="main"),
    path('create_good/', good_create_view, name="good_add"),
    path('good_view/<int:pk>/', good_view_, name="good_view")
]