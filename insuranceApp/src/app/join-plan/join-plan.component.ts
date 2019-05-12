import { Component, OnInit } from '@angular/core';
import { sha256, sha224 } from 'js-sha256';
import { ActivatedRoute } from '@angular/router';
import { map }            from 'rxjs/operators';
import { Router, NavigationExtras } from '@angular/router';

@Component({
  selector: 'app-join-plan',
  templateUrl: './join-plan.component.html',
  styleUrls: ['./join-plan.component.css']
})
export class JoinPlanComponent implements OnInit {
  userAddr: string;
  balance: number;
  toggle: true;
  TxID: string;
  amount: number;
  selectedPlan: string = "";

  constructor(private route: ActivatedRoute, private router: Router) { }

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
      .pipe(map(params => this.balance = parseInt(params.get('balance') || '0')))
      .subscribe(balance => {
        console.log(balance)
        this.balance = balance
      })
  }

  join():void {
    this.waits(3000);
    this.TxID = sha256(this.amount.toString());
    this.toggle = true;
    this.balance -= this.amount;
  }

  waits(ms): void{
    var start = new Date().getTime();
    var end = start;
    while(end < start + ms) {
      end = new Date().getTime();
   }
 }

}
