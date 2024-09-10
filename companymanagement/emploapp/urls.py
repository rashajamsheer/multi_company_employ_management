from django.urls import path
from .views import employee_list, employee_create, employee_update, employee_delete, role_list, role_create, \
    role_update, role_delete, department_list, department_create, department_update, department_delete, \
    profile_view, leave_request_view, clock_in_view, clock_out_view
app_name='emploapp'
urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('new/', employee_create, name='employee_create'),
    path('edit/<int:pk>/', employee_update, name='employee_update'),
    path('delete/<int:pk>/', employee_delete, name='employee_delete'),


    path('department/', department_list, name='department_list'),
    path('department/create/', department_create, name='department_create'),
    path('department/<int:pk>/update/', department_update, name='department_update'),
    path('department/<int:pk>/delete/', department_delete, name='department_delete'),


    path('roles/', role_list, name='role_list'),
    path('roles/create/', role_create, name='role_create'),
    path('roles/<int:pk>/update/', role_update, name='role_update'),
    path('roles/<int:pk>/delete/', role_delete, name='role_delete'),

    path('profile/', profile_view, name='profile'),
    path('clock_in/', clock_in_view, name='clock_in'),
    path('clock_out/', clock_out_view, name='clock_out'),
    path('leave/request/', leave_request_view, name='leave_request'),
]