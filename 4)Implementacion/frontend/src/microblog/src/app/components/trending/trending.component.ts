import { Component, OnInit } from '@angular/core';
import {HashtagTendenciaService, MensajesTendenciaService} from './../../services/post.service'

@Component({
  selector: 'app-trending',
  templateUrl: './trending.component.html',
  styleUrls: ['./trending.component.css']
})
export class TrendingComponent implements OnInit {
  arrayTendencias: any;
  arrayMensajes: any
  

  constructor(
    private HashtagTendenciaService: HashtagTendenciaService,
    private MensajesTendenciaService: MensajesTendenciaService
    
  ) { }

  ngOnInit(): void {

    this.HashtagTendenciaService.getHashtagTendencia().subscribe(
      (data:any) => {
        console.log('JSON data: ', data);
        this.arrayTendencias = data;
      }
    )

    this.MensajesTendenciaService.getMensajesTendencia().subscribe(
      (data:any) => {
        console.log('JSON data: ', data);
        this.arrayMensajes = data;
      }
    )

  }

}
