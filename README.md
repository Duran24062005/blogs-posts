<p align="center">
  <a href="">
    <img src="https://miro.medium.com/v2/resize:fit:786/format:webp/1*dpXAaEpwsJcs2UbZEp5jJw.png" height="96">
    <h3 align="center">Back-End BlogPost in FastAPI Starter</h3>
  </a>
</p>

<p align="center">BlogPosts backend simple desarrollado en <a href="https://fastapi.tiangolo.com/">FastAPI</a> as the API backend.</p>

<br/>

# Introduction

En este repositorio encontraras toda una estructura de BackEnd desarrollada en Pyhton utilizando FastAPI, sugiendo convenciones de uso profesional, por lo que te podría servir de güia.

Este es un sistema de blogs en el cual se puede hacer un CRUD ``(Crear = Create, Leer = Read, Actualizar = Update y Borrar = Delete)``.

Todo esto se logra haciendo peticiones desde el Frontend a el Backend, en donde este le hace peticiones mediante protocolo de comunicación. De estos protocolos hay varios como los son el que será utilizado aquí llamado `HTTP`, los demas protocolos son WebSocket, Socket.io, entre otros.

## ¿Qué es el protocolo HTTP?

El protocolo HTTP es aquel que define un conjunto de métodos de petición que indican la acción que se desea realizar para un recurso determinado del servidor.

### ¿Cules son los principales meteodos?

Los principales métodos soportados por HTTP y por ello usados por una API REST son:

#### `POST`: crear un recurso nuevo

#### `PUT`: modificar un recurso existente

#### `GET`: consultar información de un recurso

#### `DELETE`: eliminar un recurso

Como te diste cuenta con estos métodos podemos empezar a crear un CRUD en nuestra aplicación.

### ¿De qué tratará nuestra API?

El proyecto que está aquí construido es una API que nos brindará información relacionada con una serie de blogposts los con los cuales podremos trabajar, por lo que tendremos lo siguiente:

### Consulta de todos los Posts

Para lograrlo utilizaremos el método GET y solicitaremos todos los datos de nuestros posts.

### Filtrado de Posts

También solicitaremos información de posts por su id y por la categoría a la que pertenecen, para ello utilizaremos el método GET y nos ayudaremos de los parámetros de ruta y los parámetros query.

### Registro de peliculas

Usaremos el método POST para registrar los datos de nuestros posts y también nos ayudaremos de los esquemas de la librería pydantic para el manejo de los datos.

### Modificación y eliminación

Finalmente para completar nuestro CRUD realizaremos la modificación y eliminación de datos en nuestra aplicación, para lo cual usaremos los métodos PUT y DELETE respectivamente.

Y lo mejor es que todo esto lo estarás construyendo mientras aprendes FastAPI.

<a href="https://github.com/Duran24062005">Alexi Dg - python</a>
