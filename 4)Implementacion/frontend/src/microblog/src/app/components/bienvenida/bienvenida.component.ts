import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'
import {AuthService} from './../../services/auth.service'
import { Router } from '@angular/router';
import jwt_decode from 'jwt-decode';


@Component({
  selector: 'app-bienvenida',
  templateUrl: './bienvenida.component.html',
  styleUrls: ['./bienvenida.component.css']
})

export class BienvenidaComponent implements OnInit {

  registrarForm: any;
  loginForm: any;

  constructor(
    private AuthService: AuthService,
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      email: ["asd@gmail.com", Validators.required],
      contra: ["123", Validators.required],
    })
    this.registrarForm = this.formBuilder.group({
      email: ["messi@gmail.com", Validators.required],
      contra: ["123", Validators.required],
      alias: ["Messirve", Validators.required],
      nombre: ["Messi", Validators.required],
      foto: [""],
      descripcion: [""],
    })
  }


  submitlogin() {
    if(this.loginForm.valid) {
      this.login(
        {
          correo:this.loginForm.value.email, 
          password: this.loginForm.value.contra
        }
      )
    }
  }

  submitregistrar() {
    if(this.loginForm.valid) {
    this.registrar(
        {
          correo: this.registrarForm.value.email,
          alias: this.registrarForm.value.alias,
          nombre: this.registrarForm.value.nombre,
          password: this.registrarForm.value.contra,
          descripcion: this.registrarForm.value.descripcion,
          foto: this.registrarForm.value.foto
        }
      )
    }
  }

  login(dataLogin:any) {
    console.log('Comprobando credenciales...');
    this.AuthService.login(dataLogin).subscribe(
      {
        next: (rta) => {
          localStorage.setItem('token', rta.access_token) ;
          // this.router.navigate(["home"])
        }, 
        
        error: (error) =>{
          alert('Credenciales incorrectas');
          console.log('Error: ', error);
          localStorage.removeItem('token');
    
        }, 
        
        complete: () => {
          console.log('Terminó el login');
        }
      }
    )
  }

  registrar(dataLogin:any) {
    console.log('Comprobando credenciales...');
    this.AuthService.register(dataLogin).subscribe(
      {
        next: (rta) => {
          localStorage.setItem('token', rta.access_token) ;
          // this.router.navigate(["home"])
        }, 
        
        error: (error) =>{
          alert('Credenciales incorrectas');
          console.log('Error: ', error);
          localStorage.removeItem('token');
    
        }, 
        
        complete: () => {
          console.log('Termino el registrado');
        }
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

