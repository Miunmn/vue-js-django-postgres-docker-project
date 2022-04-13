# Destacame Buses
Este proyecto fue realizado para poder registrar buses, trayectos, conductores y buses de una empresa 
transportes.

### Dependecias
Se utiliza Docker para ejecutar el proyecto.
- Docker

### Guía de instalación
Para la instalación se asume que se ejecuta en un environment de Linux.
```bash
sudo docker-compose up --build
```

### Errores frecuentes
Para construir el contenedor de postgres, podría suceder que el puerto de la computadora 
host está utilizando el puerto 5432 (puerto default de postgres), lo que generaría un error al momento 
de ejecutar ``` bash sudo docker-compose up --build ```, por lo que se tendría que detener el proceso que use ese puerto.

```bash sudo lsof -i :5432 ```
 y obtenemos el process ID que utiliza el puerto 5432, y lo detenemos
```bash sudo kill <Process ID>```
y volvemos a ejecutar
```bash
sudo docker-compose up --build
```

Tambien podría pasar que el contenedor de la backend buildee más rápido que la base de datos, por lo que sería cuestión de 
intentar buildear de nuevo el proyecto con 
```bash
sudo docker-compose up --build
```

### Modelo de Datos
Diagrama ER
![Diagrama ER](./ER-Diagram.png)

