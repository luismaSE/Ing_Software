import { Component, OnInit } from '@angular/core';
import {HashtagTendenciaService} from './../../services/post.service'

@Component({
  selector: 'app-trending',
  templateUrl: './trending.component.html',
  styleUrls: ['./trending.component.css']
})
export class TrendingComponent implements OnInit {
  arrayTendencias: any;
  longitud: any;
  arrayEjemplo: any;
  

  constructor(
    private HashtagTendenciaService: HashtagTendenciaService
    
  ) { }

  ngOnInit(): void {
    this.HashtagTendenciaService.getHashtagTendencia().subscribe(
      (data:any) => {
        console.log('JSON data: ', data);
        this.arrayTendencias = data;
        this.arrayEjemplo = [{"hola":"hola"},{"chau":"chau"}];
      }
    )
  }

}
