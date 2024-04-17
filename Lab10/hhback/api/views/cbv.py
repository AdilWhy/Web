from django.http import JsonResponse
from django.views import View
from ..models import Company, Vacancy
from django.core import serializers
# Create your views here.


class CompanyList(View):
    def get(self, request):
        companies = Company.objects.all()
        json = {'companies': [company.name for company in companies]}
        return JsonResponse(json, json_dumps_params={'ensure_ascii': False})


class CompanyDetail(View):
    def get(self, request, id):
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        company_json = serializers.serialize('json', company)
        return JsonResponse(company_json, safe=False, json_dumps_params={'ensure_ascii': False})


class CompanyVacancies(View):
    def company_vacancies(request, id):
        company = Company.objects.get(id=id)
        vacancies = company.vacancy_set.all()
        vacancies_json = [{'id': vacancy.id, 'name': vacancy.name,
                           'salary': vacancy.salary} for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False, json_dumps_params={'ensure_ascii': False})


class VacanciesList(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        json = [{'vacancies': vacancy.name, 'company': vacancy.company.name}
                for vacancy in vacancies]
        return JsonResponse(json, safe=False, json_dumps_params={'ensure_ascii': False})


class VacancyDetail(View):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        vacancy_json = serializers.serialize('json', vacancy)
        return JsonResponse(vacancy_json, safe=False, json_dumps_params={'ensure_ascii': False})


class TopTenVacancies(View):
    def get(self, request):
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        vacancies_json = [{'name': vacancy.name, 'salary': vacancy.salary,
                           'company': vacancy.company.name} for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False, json_dumps_params={'ensure_ascii': False})
