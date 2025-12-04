from django.contrib import admin
from django.urls import path
from medapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Doctors
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/edit/<int:id>/', views.edit_doctor, name='edit_doctor'),
    path('doctors/delete/<int:id>/', views.delete_doctor, name='delete_doctor'),

    # Patients
    path('patients/', views.patients, name='patients'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/edit/<int:id>/', views.edit_patient, name='edit_patient'),
    path('patients/delete/<int:id>/', views.delete_patient, name='delete_patient'),

    # Appointments
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/edit/<int:id>/', views.edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:id>/', views.delete_appointment, name='delete_appointment'),
]



