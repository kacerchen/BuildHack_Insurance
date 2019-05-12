import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { JoinPlanComponent } from './join-plan.component';

describe('JoinPlanComponent', () => {
  let component: JoinPlanComponent;
  let fixture: ComponentFixture<JoinPlanComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ JoinPlanComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(JoinPlanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
