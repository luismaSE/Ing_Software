import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'
import {MensajesService} from './../../services/post.service'
import { Router } from '@angular/router';
import jwt_decode from 'jwt-decode';

@Component({
  selector: 'app-muro',
  templateUrl: './muro.component.html',
  styleUrls: ['./muro.component.css']
})
export class MuroComponent implements OnInit {

  alias: any;
  mensajes: any;
  token: any
  arrayMensajes: any;

  constructor(
    private MensajesService: MensajesService
  ) { }

  ngOnInit(): void {
    
    // localStorage.setItem('token', "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4OTU5OTg1MSwianRpIjoiYjgzOGE1MzktNzlmMS00ZDIzLWI2ZGQtNTc0OWRkMzNlMTQ1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InBlcGVAZ21haWwuY29tIiwibmJmIjoxNjg5NTk5ODUxLCJleHAiOjE2ODk2MTUwOTEsImFkbWluIjowLCJjb3JyZW8iOiJwZXBlQGdtYWlsLmNvbSIsImFsaWFzIjoicGVwZSIsImRlc2NyaXBjaW9uIjoiIiwiZm90byI6IiJ9.h74u7A1_Dem9POKW0oCeAvdZOhWdwkDyDJceswstLg4")
    this.token = localStorage.getItem("token") || undefined
    this.MensajesService.getMensajes(this.token).subscribe(
      (data:any) => {
        console.log('JSON data: ', data);
        this.arrayMensajes = data;
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
}
