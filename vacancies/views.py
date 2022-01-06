from django.http import Http404
from django.shortcuts import render

import data
from vacancies.models import Vacancy, Specialty, Company


def main_view(request):
    '''
    Функция представления для главной страницы.
    View function for main page of site.
    :param request:
    :return:
    '''
    return render(request,
                  'index.html',
                  context={'specialties': Specialty.objects.all(),
                           'companies': Company.objects.all(),
                           })


def all_vacancies_view(request):
    '''
    Функция представления для страницы со всеми вакансиями.
    View function for page with all vacancies.
    :param request:
    :return:
    '''
    return render(request,
                  'vacancies.html',
                  context={'vacanсies_count': Vacancy.objects.count(),
                           'vacanсies': Vacancy.objects.all(),
                           })


def vacancies_cat_view(request, specialization: str):
    '''
    Функция представления для страницы с вакансиями опредленного направления (specialization).
    View function for page with vacancies of one direction.
    :param specialization: название направление
    :param request:
    :return:
    '''
    valid_specialization = tuple(item.code for item in Specialty.objects.all())
    if specialization not in valid_specialization:
        raise Http404
    id_specialty = getattr(Specialty.objects.get(code=specialization), 'id')

    return render(request,
                  'vacancies_by_specialization.html',
                  context={'specialization': specialization,
                           'vacancies': Vacancy.objects.filter(specialty_id=id_specialty),
                           'id_specialty': id_specialty,
                           'specialization_info': Specialty.objects.get(code=specialization),
                           'vacancies_count': Vacancy.objects.filter(specialty_id=id_specialty).count(),
                           })


def companies_view(request, company_id: int):
    '''
    Функция представления для страницы с информацией о компании и её вакансиях.
    View function for page with information about company and its vacancies.
    :param company_id:
    :param request:
    :return:
    '''
    valid_company_id = tuple(item.id for item in Company.objects.all())
    if company_id not in valid_company_id:
        raise Http404
    return render(request,
                  'company.html',
                  context={'company_info': Company.objects.get(id=company_id),
                           'vacancy_count': Vacancy.objects.filter(company_id=company_id).count(),
                           'vacancies_of_company': Vacancy.objects.filter(company_id=company_id),
                           })


def vacancy_view(request, vacancy_id: int):
    '''
    Функция представления для страницы с информацией о вакансии.
    View function for page with vacancy information.
    :param vacancy_id:
    :param request:
    :return:
    '''
    valid_vacancy_id = tuple(item.id for item in Vacancy.objects.all())
    if vacancy_id not in valid_vacancy_id:
        raise Http404
    id_company = Vacancy.objects.get(id=vacancy_id).company_id
    return render(request, 'vacancy.html',
                  context={'vacancy': Vacancy.objects.get(id=vacancy_id),
                           'company_info': Company.objects.get(id=id_company)})
