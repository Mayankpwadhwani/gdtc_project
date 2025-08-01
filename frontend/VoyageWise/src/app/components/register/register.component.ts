import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { RouterLink, RouterOutlet } from '@angular/router';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';
import { Router } from '@angular/router';


@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule,
    RouterOutlet,RouterLink,NavbarComponent,FooterComponent],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  user = {
    name: '',
    email: '',
    password: ''
  };
  

  constructor(private http: HttpClient,private router: Router) {}

  onSubmit() {
    this.http.post('http://localhost:8000/register', this.user).subscribe({
      next: (response) => {
        alert('Registration successful!');
        this.router.navigate(['/login']); 
      },
      error: (error) => {
        alert(error.error.detail || 'Registration failed');
      }
    });
  }
}
