import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { identifierName } from '@angular/compiler';

@Injectable({
  providedIn: 'root'
})

//! Rutas del backend
// api.add_resource(resources.UsuarioResource, '/usuario/<alias>')     #Get, put

export class UsuarioService {
  private url = "http://127.0.0.1:7500/usuario"

  constructor(
    private httpClient: HttpClient
  ) { }

  getUsuario(alias: string) {
    return this.httpClient.get(this.url + "/" + alias);
  }

  putUsuario(data: any, token:string, alias: string) {
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.put(this.url + "/" + alias, data, {headers: heads});
  }

}

// api.add_resource(resources.UsuariosResource, "/usuarios")   #Get

export class UsuariosService {
  url = "usuarios"

  constructor(
    private httpClient: HttpClient
  ) { }

  getUsuarios(token: string) {
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.get(this.url, {headers: heads});
  }
}

// api.add_resource(resources.UsuariosEncontradosResource, "/usuariosencontrados/<alias>")     #Get

export class UsuariosEncontradosService {
  url = "usuariosencontrados"

  constructor(
    private httpClient: HttpClient
  ) { }

  getUsuario(alias: string) {
    return this.httpClient.get(this.url + "/" + alias);
  }

}

// api.add_resource(resources.MensajesResource, "/mensajes")    #Post, get

@Injectable({
  providedIn: 'root'
})

export class MensajesService {
  url = "http://localhost:7500/mensajes"

  constructor(
    private httpClient: HttpClient
  ) { }

  postMensajes(data: any, token: any) {
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.post(this.url, data, {headers: heads})
  }

  getMensajes(token: string) {
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.get(this.url, {headers: heads});
  }

}

// api.add_resource(resources.MensajeResource, "/mensaje/<_id>")    #Delete, #put

export class MensajeService {
  url = "mensaje"

  constructor(
    private httpClient: HttpClient
  ) { }
  
  deleteMensaje(token: string, id: number) { 
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.delete(this.url + "/" + id.toString(), {headers: heads})
  }  

  putMensaje(data: any, token:string, id: number) {
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.put(this.url + "/" + id.toString(), data, {headers: heads});
  }
}

// api.add_resource(resources.MensajesAutorResource, "/mensajes/<autor>")  #Get

export class MensajesAutorService {
  url = "mensajes"

  constructor(
    private httpClient: HttpClient
  ) { }

  getMensajes(alias: string) {
    return this.httpClient.get(this.url + "/" + alias);
  }
}

// api.add_resource(resources.DiasResource, "/dias") #Get, #put

export class DiasService {
  url = "dias"

  constructor(
    private httpClient: HttpClient
  ) { }

  getDias() {
    return this.httpClient.get(this.url);
  }

  putDias(data: any, token:string) {
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.put(this.url, data, {headers: heads});
  }

}


// api.add_resource(resources.HashtagTendenciaResource, "/hashtagtendencia") #Get, #post
@Injectable({
  providedIn: 'root'
})

export class HashtagTendenciaService {
  url = "http://localhost:7500/hashtagtendencia"

  constructor(
    private httpClient: HttpClient
  ) { }

  getHashtagTendencia() {
    return this.httpClient.get(this.url);
  }

  postHashtagTendencia(token: string) {
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.post(this.url, {headers: heads})
  }

}

// api.add_resource(resources.MensajePrivadoResource, "/mensajeprivado")   #Get, #post

@Injectable({
  providedIn: 'root'
})

export class MensajePrivadoService {
  url = "http://localhost:7500/mensajeprivado"

  constructor(
    private httpClient: HttpClient
  ) { }

  postMensajePrivado(data: any, token: string) {
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.post(this.url, data, {headers: heads})
  }

}

// TODO Servicios: Mensajes privados, Contacto OK
// api.add_resource(resources.MensajesPrivadosContactoResource, "/mensajesprivadoscontacto/<contacto>") #Get

@Injectable({
  providedIn: 'root'
})

export class MensajesPrivadosContactoService {
  url = "http://localhost:7500/mensajesprivadoscontacto"

  constructor(
    private httpClient: HttpClient
  ) { }

  getMensajes(contacto: string, token: string) {
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.get(this.url + "/" + contacto, {headers: heads});
  }

}
// api.add_resource(resources.ContactosResource, "/contactos")   #Get

@Injectable({
  providedIn: 'root'
})

export class ContactosService {
  url = "http://localhost:7500/contactos"

  constructor(
    private httpClient: HttpClient
  ) { }

  getContactos(token: string) {
    let heads = new HttpHeaders().set('Content-Type', 'application/json').set('Access-Control-Allow-Origin', '*').set('Authorization', 'Bearer ' + token)
    return this.httpClient.get(this.url, {headers: heads});
  }

}



