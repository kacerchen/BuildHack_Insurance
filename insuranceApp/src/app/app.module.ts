import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { SignupComponent } from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { PolicyListComponent } from './policy-list/policy-list.component';
import { PolicyDetailsComponent } from './policy-details/policy-details.component';
import { ClaimComponent } from './claim/claim.component';

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    LoginComponent,
    PolicyListComponent,
    PolicyDetailsComponent,
    ClaimComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
