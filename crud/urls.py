from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_list, name = "emp_list"),
    path('empi', views.emp_insert, name = "emp_insert"),
    path('<int:id>/', views.emp_insert, name = "emp_update"),
    path('del/<int:id>', views.emp_del, name = "emp_delete")
]