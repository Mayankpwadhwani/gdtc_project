import { Routes } from '@angular/router';


export const routes: Routes = [
{
    path: 'login',
    loadComponent: () =>
      import('./login/login.component').then(m => m.LoginComponent)
  },
  {
    path: 'register',
    loadComponent: () =>
      import('./register/register.component').then(m => m.RegisterComponent)
  },
  
  {
    path: '',
    loadComponent: () =>
      import('./home/home.component').then(m => m.HomeComponent)
  },
  {
    path: 'home',
    loadComponent: () =>
      import('./home/home.component').then(m => m.HomeComponent)
  },
  {
    path: 'contact',
    loadComponent: () =>
      import('./contact/contact.component').then(m => m.ContactComponent)
  },
  {
    path: 'list',
    loadComponent: () =>
      import('./list/list.component').then(m => m.ListComponent)
  },
  {
    path: 'services',
    loadComponent: () =>
      import('./services/services.component').then(m => m.ServicesComponent)
  },
  {
    path: 'offers',
    loadComponent: () =>
      import('./offers/offers.component').then(m => m.OffersComponent)
  },
  {
    path: 'bookings',
    loadComponent: () =>
      import('./bookings/bookings.component').then(m => m.BookingsComponent)
  },
  {
    path: 'mybooking',
    loadComponent: () =>
      import('./mybooking/mybooking.component').then(m => m.MybookingComponent)
  },
    
];
