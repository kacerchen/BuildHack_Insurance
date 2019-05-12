import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { map }            from 'rxjs/operators';

@Component({
  selector: 'app-claim',
  templateUrl: './claim.component.html',
  styleUrls: ['./claim.component.css']
})
export class ClaimComponent implements OnInit {

  userAddr: string;
  balance: number;

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    this.route
      .queryParamMap
      .pipe(map(params => params.get('userAddress') || 'None'))
      .subscribe(address => {
        console.log(address)
        this.userAddr = address
      })

      this.route
      .queryParamMap
      .pipe(map(params => this.balance = parseInt(params.get('balance') || 'None')))
      .subscribe(balance => {
        console.log(balance)
        this.balance = balance
      })
  }

}
