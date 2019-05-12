import { Component, OnInit } from '@angular/core';
import { Router, NavigationExtras } from '@angular/router';
import { USERS } from '../mock-users';
import { User } from '../user';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username: string;
  password: string;

  constructor(private router: Router) { }

  ngOnInit() {
  }

  login(): void {
    let currentUser = this.findUser(this.username);

    if(currentUser) {
      let navigationExtra: NavigationExtras = {
        queryParams: { 'userAddress': currentUser.address, 'balance': currentUser.balance, 'user': currentUser }
      }

      this.router.navigate(['/join'], navigationExtra)      
    } else {
      this.router.navigate(['/signup'])
    }
  }

  findUser(username: string): User{
    return USERS.find(user => user.username == username);
  }

}
