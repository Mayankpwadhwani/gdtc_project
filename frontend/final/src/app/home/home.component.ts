import { Component } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink, RouterOutlet } from '@angular/router';
import { TravelService } from '../travel.service';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';
import { FooterComponent } from '../footer/footer.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule,
     RouterOutlet,RouterLink,FooterComponent],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  mode = 'bus';
  fromCity = '';
  toCity = '';
  date = '';
  travelClass = 'Economy'; 
  passengers = 1;          
  results: any[] = [];
  loading = false;
  errorMessage = '';


  constructor(private http: HttpClient,
     private travelData: TravelService,
  private router: Router,private authService: AuthService
  ) {


  }

  search() {
    const apiUrl = 'http://localhost:8000/search';

    let params = new HttpParams()
      .set('mode', this.mode)
      .set('from_city', this.fromCity)
      .set('to_city', this.toCity);

    if (this.date) {
      params = params.set('day', this.date);
    }

    this.loading = true;
    this.errorMessage = '';
    this.results = [];

    this.http.get(apiUrl, { params }).subscribe({
      next: (data: any) => {
        
    this.travelData.setResults(data);
    this.loading = false;
    this.router.navigate(['/list']);
      },
      error: (err) => {
        this.loading = false;
        this.errorMessage = 'Error fetching transport data. Please try again.';
        console.error('Error:', err);
      }
    });
  }
  
logout() {
  this.authService.logout();
  localStorage.removeItem('access_token');
  alert("Logged Out Successfully")//snackbar
  this.router.navigate(['/login']);
}

}
