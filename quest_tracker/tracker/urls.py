from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('registerpage/', views.registerpage,name='registerpage'),
    path('approve/<int:id>/', views.approve),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('manager_login/', views.manager_login, name='manager_login'),
    path('manager/', views.manager,name='manager'),
    path('create_task/', views.create_task, name='create_task'),
    path('task_list/', views.task_list, name='task_list'),
    path('update_task_status/<int:task_id>/', views.update_task_status, name='update_task_status'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

]
