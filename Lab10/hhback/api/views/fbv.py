from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Vacancy
from django.core import serializers


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = serializers.serialize('json', companies)
        return JsonResponse(companies_json, safe=False)


@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        company_json = serializers.serialize('json', [company])
        return JsonResponse(company_json, safe=False)


@csrf_exempt
def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    vacancies = company.vacancy_set.all()
    vacancies_json = serializers.serialize('json', vacancies)
    return JsonResponse(vacancies_json, safe=False)


@csrf_exempt
def vacancies_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = serializers.serialize('json', vacancies)
        return JsonResponse(vacancies_json, safe=False)


@csrf_exempt
def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        vacancy_json = serializers.serialize('json', [vacancy])
        return JsonResponse(vacancy_json, safe=False)


@csrf_exempt
def top_ten_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        vacancies_json = serializers.serialize('json', vacancies)
        return JsonResponse(vacancies_json, safe=False)
