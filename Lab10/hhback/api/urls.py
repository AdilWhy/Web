from django.urls import path
from api.views import cbv

urlpatterns = [
    path('companies/', cbv.CompanyList.as_view(), name='companies_list'),
    path('companies/<int:id>/', cbv.CompanyDetail.as_view(), name='company_detail'),
    path('companies/<int:id>/vacancies/', cbv.CompanyVacancies.as_view(), name='company_vacancies'),
    path('vacancies/', cbv.VacanciesList.as_view(), name='vacancies_list'),
    path('vacancies/<int:id>/', cbv.VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancies/top_ten/', cbv.TopTenVacancies.as_view(), name='top_ten_vacancies'),
]