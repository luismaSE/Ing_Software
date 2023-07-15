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
    
    localStorage.setItem('token', "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4OTQ1NzU4OSwianRpIjoiYjE1ZTk3MzYtYzhkNC00Y2IyLWIzN2UtODc1ZTY3NjhhYTAxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InBlcGVAZ21haWwuY29tIiwibmJmIjoxNjg5NDU3NTg5LCJleHAiOjE2ODk0NzI4MjksImFkbWluIjowLCJjb3JyZW8iOiJwZXBlQGdtYWlsLmNvbSIsImFsaWFzIjoicGVwZSIsImRlc2NyaXBjaW9uIjoiIiwiZm90byI6IiJ9.4pIibBBeuMXoIR5kO4_r1XdmhrUf_8P__Pb3jLnz9lQ")
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
