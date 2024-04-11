import { Injectable } from '@angular/core';
import {CanActivate, Router} from '@angular/router';
import {ActivatedRouteSnapshot, RouterStateSnapshot} from '@angular/router';
import {AuthService} from './auth.service'

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService implements CanActivate {

  constructor(
    private router: Router,
    private auth: AuthService
  ) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    // If the user is authenticated, just skip
    console.log('Checking if the user is authenticated');
    if (this.auth.isAuthenticated()) {
      console.log('User is authenticated');
      return true;
    }

    console.log('User is not authenticated. Redirecting to login');
    const redirectUrl = state.url;
    // noinspection JSIgnoredPromiseFromCall
    this.router.navigateByUrl(
      this.router.createUrlTree(['/login'], {queryParams: {redirectUrl}})
    );

    return false;
  }
}
