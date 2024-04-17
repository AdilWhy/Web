import { Company } from "./company";

export interface Vacancy {
    name: string;
    description: string;
    salary: number;
    company: Company;
  }