import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from '../auth.service';
import { DEFAULT_ROUTE } from '../app-routing.module';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup = this.formBuilder.group({
    username: [null, Validators.required],
    password: [null, Validators.required]
  });
  showError = false;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private route: ActivatedRoute,
    private auth: AuthService
  ) { }

  ngOnInit(): void {}

  submit(): void {
    // Check if the inputed data is valid
    if (!this.loginForm.valid) {
      return;
    }

    // Disable errors
    this.showError = false;

    // Execute the authentication with the API
    const formData = this.loginForm.value;
    this.auth.authenticate(
      formData.username,
      formData.password
    ).subscribe(() => {
      console.log('The login was successful.');
      this.route.queryParams.subscribe(params => {
        const targetUrl = params.redirectUrl ? params.redirectUrl : DEFAULT_ROUTE;
        console.log(`Redirecting to ${targetUrl}`);
        this.router.navigateByUrl(targetUrl).then();
      });
    }, (error) => {
      console.error('Failed to login.');
      console.error(error);
      this.showError = true;
    })
  }
}
