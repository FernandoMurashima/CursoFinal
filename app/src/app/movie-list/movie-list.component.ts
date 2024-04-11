import { Component, OnInit } from '@angular/core';
import {Movie, MoviesService} from '../movies.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.scss']
})
export class MovieListComponent implements OnInit {

  movies: Array<Movie> |undefined;
  searchPattern: string ='';

  constructor(
    private moviesSrv: MoviesService,
  ) { }

  ngOnInit(): void {
    this.loadMovies();
  }

  loadMovies(){
    this.moviesSrv.load(this.searchPattern).subscribe((movies: Movie[])  => {
      this.movies = movies;
    });

  }

  clearSearch(): void{
    this.searchPattern='';
  }

  onSearchChange(): void{
    this.loadMovies();
  }
  

}
