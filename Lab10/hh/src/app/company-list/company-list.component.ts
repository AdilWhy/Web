import { Component, OnInit } from '@angular/core';
import { Company } from '../company'
import { CompanyService } from '../company.service';
import { NgFor } from '@angular/common';
import { response } from 'express';

@Component({
  selector: 'app-company-list',
  standalone: true,
  imports: [
    NgFor
  ],
  templateUrl: './company-list.component.html',
  styleUrl: './company-list.component.css'
})
export class CompanyListComponent implements OnInit{
  companies: Company[] = [{
    name: 'Company 1',
    description: 'Description 1',
    city: 'City 1',
    address: 'Address 1',
  }];

  constructor(private companyService: CompanyService) {}

  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies(): void {
    this.companyService.getCompanies()
      .subscribe((response: any) => this.companies = response.companies);
  }
}
