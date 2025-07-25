import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Router, RouterLink, RouterModule, RouterOutlet } from '@angular/router';
import { AuthService } from '../auth.service';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule,
    RouterModule,RouterLink,NavbarComponent,RouterOutlet,FooterComponent],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email = '';
  password = '';
  errorMessage = '';
  

  constructor(private http: HttpClient, private router: Router,
    private authService: AuthService  ) {}



  onSubmit() {
    const payload = { email: this.email, password: this.password };
    this.http.post<any>('http://127.0.0.1:8000/login', payload).subscribe({
      next: (response) => {
        localStorage.setItem('access_token', response.access_token);
      this.errorMessage = ''; 
      alert('Logged in successfully!');
      this.authService.setLoginStatus(true);
        this.router.navigate(['/home']); 
        

      },
      error: (error) => {
        this.errorMessage = error.error.detail || 'Login failed';
      },
    });
  }
}
