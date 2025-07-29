
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TravelService {
  private results: any[] = [];

  setResults(data: any[]) {
    this.results = data;
  }

  getResults(): any[] {
    return this.results;
  }
}
