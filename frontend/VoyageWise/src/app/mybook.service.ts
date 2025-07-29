import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MybookService {
private apiUrl = 'http://localhost:8000/bookingdetails';

      constructor(private http: HttpClient) { }

      getItems(): Observable<any> {
        return this.http.get(`${this.apiUrl}`);
      }
    }