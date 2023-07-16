import { Component, OnInit } from '@angular/core';
import {MensajesPrivadosContactoService, ContactosService, MensajePrivadoService} from './../../services/post.service'
import jwt_decode from 'jwt-decode';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'

@Component({
  selector: 'app-mensaje-privado',
  templateUrl: './mensaje-privado.component.html',
  styleUrls: ['./mensaje-privado.component.css']
})
export class MensajePrivadoComponent implements OnInit {

  token: any
  arrayContactos: any;
  cantidadContactos: any;
  numbers: any;
  arrayMensajes: any;
  contacto: any
  mensajeForm: any;
  primero: any;
 

  constructor(

    private MensajesPrivadosContactoService: MensajesPrivadosContactoService,
    private ContactosService: ContactosService,
    private MensajePrivado: MensajePrivadoService,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    
    localStorage.setItem('token', "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4OTUzNTE1MiwianRpIjoiNTEwMjFkYTktZjc5ZS00ZmEyLTgxY2MtNmRhZTcyNWU0NDM5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InBlcGVAZ21haWwuY29tIiwibmJmIjoxNjg5NTM1MTUyLCJleHAiOjE2ODk1NTAzOTIsImFkbWluIjowLCJjb3JyZW8iOiJwZXBlQGdtYWlsLmNvbSIsImFsaWFzIjoicGVwZSIsImRlc2NyaXBjaW9uIjoiIiwiZm90byI6IiJ9.KUUw-_vWpQ_f1mk_LlKqXj1C5FajVtT3sc6QNXJZQ5Y")
    this.token = localStorage.getItem("token") || undefined
    this.ContactosService.getContactos(this.token).subscribe(
      (data:any) => {
        console.log('JSON data: ', data);
        this.arrayContactos = data;
        this.cantidadContactos = data.contactos.length
        this.numbers = Array.from({ length: this.cantidadContactos }, (_, i) => i);


        this.primero= this.arrayContactos["contactos"][0]
      
        this.MensajesPrivadosContactoService.getMensajes(this.primero,this.token).subscribe(
          (data:any) => {
            console.log('JSON data mensajes: ', data);
            this.arrayMensajes = data;
            this.contacto = this.primero
            
          }
        )


      }
    )
    this.mensajeForm = this.formBuilder.group({
      texto: ["", Validators.required],
    
    } )
  
  }

  submit(alias:any) {
    this.MensajesPrivadosContactoService.getMensajes(alias,this.token).subscribe(
      (data:any) => {
        console.log('JSON data mensajes: ', data);
        this.arrayMensajes = data;
        this.contacto = alias
        
      }
    )

  }

  getDecodedAccessToken(token: string): any {
    try {
      return jwt_decode(token);
    } catch(Error) {
      return null;
    }
  }

  send(destinatario:any) {
    if(this.mensajeForm.valid) {
      this.MensajePrivado.postMensajePrivado({texto:this.mensajeForm.value.texto, destinatario:destinatario},this.token).subscribe()
    }
    alert("Mensaje subido")
    this.mensajeForm = this.formBuilder.group(
      {
        texto: ["", Validators.required],
      } 
    )
  }

}
