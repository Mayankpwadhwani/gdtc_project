
import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { TravelService } from '../travel.service';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';

@Component({
  selector: 'app-list',
  standalone: true,
  imports: [CommonModule,NavbarComponent,FooterComponent],
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
  
})
export class ListComponent implements OnInit {
  results: any[] = [];

  constructor(private travelData: TravelService, private authService: AuthService, private router: Router) {}

  ngOnInit(): void {
    this.results = this.travelData.getResults();
  }
book(item: any) {
  console.log('Login status:', this.authService.isLoggedIn());

  if (!this.authService.isLoggedIn()) {
    alert('Please log in to book tickets.');
    this.router.navigate(['/login']);
    return;
  }

  console.log('Booking:', item);
  this.router.navigate(['/bookings'], { state: { travelInfo: item } });

}

}

