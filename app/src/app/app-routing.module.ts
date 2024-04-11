/* import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Movie, MoviesService } from './movies.service';

@Component({
  selector: 'app-movie-details',
  templateUrl: './movie-details.component.html',
  styleUrls: ['./movie-details.component.scss']
})
export class MovieDetailsComponent implements OnInit {

  movie: Movie | undefined;

  constructor(
    private route: ActivatedRoute,
    private movieSrv: MoviesService
  ) { }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    console.log('ID do filme:', id); // Adicione este log para verificar o valor do ID
    this.movieSrv.get(id).subscribe((movie: Movie) => {
      console.log('Detalhes do filme:', movie); // Adicione este log para verificar os detalhes do filme recebidos do serviço
      this.movie = movie;
    });
  }

} */


import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { MovieListComponent } from './movie-list/movie-list.component';
import { AuthGuardService } from './auth-guard.service';
import { MovieDetailsComponent } from './movie-details/movie-details.component';

export const DEFAULT_ROUTE = '/movie-list';

const routes: Routes = [
  { path: '', redirectTo: DEFAULT_ROUTE, pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'movie-list', component: MovieListComponent, canActivate: [AuthGuardService] },
  { path: 'movie-details/:id', component: MovieDetailsComponent, canActivate: [AuthGuardService] },
  // { path: 'movie-details/:id', component: MovieDetailsComponent },

  { path: 'error', component: MovieDetailsComponent }
  // outras rotas
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
