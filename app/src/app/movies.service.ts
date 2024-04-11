import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { NumberLiteralType } from 'typescript';
import { tap, catchError } from 'rxjs/operators';

export interface Movie {
  id: number;
  title: string;
  year: number;
  cover: string;
  description: string;
  midia: string;
  isFavorite: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class MoviesService {

  constructor(
    private http: HttpClient
  ) { }

  load(searchPattern: string): Observable<Array<Movie>> {
    let url = `${environment.apiURL}/movies`;
    if (searchPattern) {
      url += `?search=${searchPattern}`;

    }
    return this.http.get<Array<Movie>>(url);
  }

  get(id: number): Observable<Movie> {
    const url = `${environment.apiURL}/movies/${id}`;
    console.log('URL do filme:', url); 
    return this.http.get<Movie>(url);
    
  } 
 
}



