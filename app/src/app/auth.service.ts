import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environments/environment';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';


interface AuthData {
  token: string;
}


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private token: string | null;

  /**
   * Constructor
   */
  constructor(
    private http: HttpClient
  ) {
    this.token = localStorage.getItem('token');
  }

  /**
   * Returns the user token
   */
  public getToken(): string | null {
    return this.token;
  }

  /**
   * Clear the user token
   */
  public clearToken(): void {
    this.token = null;
    localStorage.removeItem('token');
  }

  /**
   * Check if there is an user authenticated
   */
  public isAuthenticated(): boolean {
    return !!this.token;
  }

  /**
   * Executes the authentication and updates the user token.
   */
  public authenticate(username: string, password: string): Observable<any> {
    const url = `${environment.apiURL}/api-token-auth/`;
    const data = {username, password};
    return this.http.post<AuthData>(url, data).pipe(map((response) => {
      this.setToken(response.token);
      return;
    }));
  }

  /**
   * Stores the user token
   */
  private setToken(value: string): void {
    this.token = value;
    localStorage.setItem('token', this.token);
  }

}
