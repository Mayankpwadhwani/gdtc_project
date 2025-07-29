import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AuthService } from 'src/app/auth.service';
import { FooterComponent } from '../footer/footer.component';
import { NavbarComponent } from '../navbar/navbar.component';

@Component({
  selector: 'app-bookings',
  standalone: true,
  imports: [FormsModule,FooterComponent,NavbarComponent],
  templateUrl: './bookings.component.html',
  styleUrls: ['./bookings.component.css']
})
export class BookingsComponent {
  travelInfo: any = {};
  booking: any = {
    customer_name: '',
    email: '',
    passengers: 1
  };

  constructor(private router: Router, private http: HttpClient, private authService: AuthService) {
    
    if (!this.authService.isLoggedIn()) {
      alert('Please log in to access bookings.');
      this.router.navigate(['/login']);
      return;
    }

  
    const nav = this.router.getCurrentNavigation();
    this.travelInfo = nav?.extras?.state?.['travelInfo'];

    
    if (!this.travelInfo) {
      alert('Missing travel details. Please select a trip again.');
      this.router.navigate(['/']);
    }
  }

  submitBooking() {
    const finalBooking = {
      ...this.travelInfo,
      ...this.booking
    };

    this.http.post('http://localhost:8000/book', finalBooking).subscribe({
      next: res => {
        console.log(' Booking successful:', res);
        alert('Booking Confirmed!');
        console.log(' travelInfo:', this.travelInfo);
        console.log(' finalBooking:', finalBooking);

    
      },
      error: err => console.error(' Error submitting booking:', err)
    });
  }
}