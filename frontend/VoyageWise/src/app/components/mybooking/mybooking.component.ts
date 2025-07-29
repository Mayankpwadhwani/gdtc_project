import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MybookService } from 'src/app/mybook.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-mybooking',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './mybooking.component.html',
  styleUrls: ['./mybooking.component.css']
})
export class MybookingComponent implements OnInit {
  items: any[] = [];
  isloggedin:boolean=false
      constructor(private mybookingService: MybookService,private router:Router) { }

      ngOnInit(): void {
        const token=localStorage.getItem('access_token');
        if(token){
          this.isloggedin=true;
        this.mybookingService.getItems().subscribe(data => {
          this.items = data;
        });}
        else{
          alert("please log in first");
          this.router.navigate(["/login"]);
        }
        
      }
    }