import { Component, OnInit } from '@angular/core';
import { UsuarioService } from './../../services/post.service'
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-mensaje',
  templateUrl: './mensaje.component.html',
  styleUrls: ['./mensaje.component.css']
})
export class MensajeComponent implements OnInit {
  datos_usuario:any;

  constructor(
    private usuarioService: UsuarioService
    ) {}

    ngOnInit(): void{
      this.usuarioService.getUsuario("pepe").subscribe(data=>{
        console.log(data)
        this.datos_usuario = data;
      }, error=>console.log(error));
    }
    
}

