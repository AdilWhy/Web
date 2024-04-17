import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CompanyListComponent } from "./company-list/company-list.component";

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.css',
    imports: [RouterOutlet, CompanyListComponent]
})
export class AppComponent {
  title = 'hh';
}
