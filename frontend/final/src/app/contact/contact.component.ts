import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink, RouterOutlet } from '@angular/router';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';
@Component({
  selector: 'app-contact',
  standalone: true,
  imports: [CommonModule, FormsModule,
    RouterLink,RouterOutlet,NavbarComponent,FooterComponent],
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent {
  name = '';
  email = '';
  message = '';

  submitForm() {
    console.log('Form submitted:', { name: this.name, email: this.email, message: this.message });
    alert('Thank you for contacting us!');
  }
}
