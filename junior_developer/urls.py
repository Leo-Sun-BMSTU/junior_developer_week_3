"""junior_developer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from vacancies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='main-view'),
    path('vacancies/', views.all_vacancies_view, name='all-vacancies-view'),
    path('vacancies/cat/<str:specialization>/', views.vacancies_cat_view, name='vacancies-cat-view'),
    path('companies/<int:company_id>', views.companies_view, name='companies-view'),
    path('vacancies/<int:vacancy_id>', views.vacancy_view, name='vacancy-view'),
]
