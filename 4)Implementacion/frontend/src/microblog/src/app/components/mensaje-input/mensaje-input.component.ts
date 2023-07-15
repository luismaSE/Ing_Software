import { Component, OnInit } from '@angular/core';
import {MensajesService} from './../../services/post.service'
import jwt_decode from 'jwt-decode';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'

@Component({
  selector: 'app-mensaje-input',
  templateUrl: './mensaje-input.component.html',
  styleUrls: ['./mensaje-input.component.css']
})
export class MensajeInputComponent implements OnInit {

  token:any;
  mensajeForm: any;
  foto:any;

  constructor(
    private MensajesService: MensajesService,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    localStorage.setItem('token', "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4OTQ1NzU4OSwianRpIjoiYjE1ZTk3MzYtYzhkNC00Y2IyLWIzN2UtODc1ZTY3NjhhYTAxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InBlcGVAZ21haWwuY29tIiwibmJmIjoxNjg5NDU3NTg5LCJleHAiOjE2ODk0NzI4MjksImFkbWluIjowLCJjb3JyZW8iOiJwZXBlQGdtYWlsLmNvbSIsImFsaWFzIjoicGVwZSIsImRlc2NyaXBjaW9uIjoiIiwiZm90byI6IiJ9.4pIibBBeuMXoIR5kO4_r1XdmhrUf_8P__Pb3jLnz9lQ")
    this.token = localStorage.getItem("token")

    console.log("\n",this.token)

    this.mensajeForm = this.formBuilder.group({
      texto: ["", Validators.required],
    
    }    
    )
  }

  submit() {
    if(this.mensajeForm.valid) {
      this.MensajesService.postMensajes({texto:this.mensajeForm.value.texto},this.token).subscribe()
    }
    alert("Mensaje subido")
    this.mensajeForm = this.formBuilder.group(
      {
        texto: ["", Validators.required],
      } 
    )
  }

  getDecodedAccessToken(token: any): any {
    try {
      return jwt_decode(token);
    } catch(Error) {
      return null;
    }
  }
}
