import { Injectable } from '@angular/core';
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest, HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

import {AuthService} from './auth.service';


@Injectable({ providedIn: 'root' })
export class TokenInterceptorService implements HttpInterceptor {

  constructor(
    private router: Router,
    private auth: AuthService
  ) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Set the variable to be returned
    let request = req;

    // If the user has a token, inject in the request
    const token = this.auth.getToken();
    if (token) {
      const newHeaders = req.headers.append('Authorization', `Token ${token}`);
      request = req.clone({headers: newHeaders});
    }
    return next.handle(request)
      .pipe(
        catchError((error: HttpErrorResponse) => {
          // If the token do not have access, clear it and navigate to app root
          if (error.status === 401) {
            console.warn('Invalid token detected.');
            this.auth.clearToken();
            window.location.href = '/';
          }
          return throwError(error);
        })
      );
  }

}
