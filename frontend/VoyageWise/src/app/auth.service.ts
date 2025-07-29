import { Injectable } from "@angular/core";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private loggedIn = false;

  constructor() {
    const storedStatus = localStorage.getItem('loggedIn');
    this.loggedIn = storedStatus === 'true';
  }

  setLoginStatus(status: boolean) {
    this.loggedIn = status;
    localStorage.setItem('loggedIn', String(status));
  }

  isLoggedIn(): boolean {
   
    this.loggedIn = localStorage.getItem('loggedIn') === 'true';
    return this.loggedIn;
  }

  logout() {
    this.loggedIn = false;
    localStorage.removeItem('loggedIn');
  }
}