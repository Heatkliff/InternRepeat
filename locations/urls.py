from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="location_index"),
    path('<int:parameter>', views.view_with_int_parameter, name="view_with_int_parameter"),
    path('<parameter>', views.view_with_parameter, name="view_with_parameter")
]
