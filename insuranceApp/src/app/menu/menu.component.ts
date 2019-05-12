import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { sha256, sha224 } from 'js-sha256';
import { map }            from 'rxjs/operators';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  
  @Input() currentAddr: string;
  @Input() currentBalance: number;
  @Input() changeAmount: number;
  TxID: string;

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
  }

  makeClaim(): void{
    this.waits(3000);
    this.TxID = sha256(this.currentBalance.toString());
    this.currentBalance += this.changeAmount;
  }

  waits(ms): void{
    var start = new Date().getTime();
    var end = start;
    while(end < start + ms) {
      end = new Date().getTime();
   }
 }

}
