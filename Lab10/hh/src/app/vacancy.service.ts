import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Vacancy } from './vacancy';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  private apiUrl = 'http://localhost:8000/api/companies';

  constructor(private http: HttpClient) { }

  getVacancies(companyId: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.apiUrl}/${companyId}/vacancies`);
  }
}
