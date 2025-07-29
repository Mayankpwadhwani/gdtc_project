import { Routes } from '@angular/router';

export const routes: Routes = [
{
    path: 'login',
    loadComponent: () =>
      import('./components/login/login.component').then(m => m.LoginComponent)
  },
  {
    path: 'register',
    loadComponent: () =>
      import('./components/register/register.component').then(m => m.RegisterComponent)
  },
  
  {
    path: '',
    loadComponent: () =>
      import('./components/home/home.component').then(m => m.HomeComponent)
  },
  {
    path: 'home',
    loadComponent: () =>
      import('./components/home/home.component').then(m => m.HomeComponent)
  },

  {
    path: 'list',
    loadComponent: () =>
      import('./components/list/list.component').then(m => m.ListComponent)
  },
  {
    path: 'services',
    loadComponent: () =>
      import('./components/services/services.component').then(m => m.ServicesComponent)
  },
  {
    path: 'offers',
    loadComponent: () =>
      import('./components/offers/offers.component').then(m => m.OffersComponent)
  },
  {
    path: 'bookings',
    loadComponent: () =>
      import('./components/bookings/bookings.component').then(m => m.BookingsComponent)
  },
  {
    path: 'mybooking',
    loadComponent: () =>
      import('./components/mybooking/mybooking.component').then(m => m.MybookingComponent)
  },
    
];
