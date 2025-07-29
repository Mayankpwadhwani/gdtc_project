import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule,RouterOutlet,RouterLink],
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  constructor(private authservice:AuthService, private router:Router){}
logout() {
  this.authservice.logout();
  localStorage.removeItem('access_token');
  alert("Logged Out Successfully")//snackbar
  this.router.navigate(['/login']);
}
}
