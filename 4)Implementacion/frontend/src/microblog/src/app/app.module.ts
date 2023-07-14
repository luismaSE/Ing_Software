import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { MensajesPrivadosComponent } from './pages/mensajes-privados/mensajes-privados.component';
import { HeaderComponent } from './components/header/header.component';
import { MuroComponent } from './components/muro/muro.component';
import { MuroUsuarioComponent } from './components/muro-usuario/muro-usuario.component';
import { MensajePrivadoComponent } from './components/mensaje-privado/mensaje-privado.component';
import { TendenciasComponent } from './components/tendencias/tendencias.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    MensajesPrivadosComponent,
    HeaderComponent,
    MuroComponent,
    MuroUsuarioComponent,
    MensajePrivadoComponent,
    TendenciasComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
