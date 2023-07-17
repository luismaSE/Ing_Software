import { UsuarioService } from './../../services/post.service'
import { ActivatedRoute } from '@angular/router';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-mensaje',
  templateUrl: './mensaje.component.html',
  styleUrls: ['./mensaje.component.css']
})
export class MensajeComponent implements OnInit {

  @Input() mensaje:any;

  constructor(
    private usuarioService: UsuarioService
    ) {}

    ngOnInit(): void{
    }
  
}

