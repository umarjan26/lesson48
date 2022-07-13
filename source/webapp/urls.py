from django.urls import path
from webapp.views import (main_view,
                          good_create_view,
                          good_view_,
                          good_update_view,
                          good_delete_view)

urlpatterns = [
    path('', main_view, name="main"),
    path('create_good/', good_create_view, name="good_add"),
    path('good_view/<int:pk>/', good_view_, name="good_view"),
    path('good_view/<int:pk>/update/', good_update_view, name="good_update"),
    path('good_view/<int:pk>/delete/', good_delete_view, name="good_delete"),
]