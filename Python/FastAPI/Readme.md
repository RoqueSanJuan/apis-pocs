Mejoras de FastAPI vs Flask

- Rendimiento:
    Es mas rapida y eficiente
    Genera automaticamente documentacion
- Tipado estatico y autocompletado:
- Documentacion interactiva
- Soporte para async await
- Validacion de datos y serializacion
- Generacion de esquemas de datos

Cuando se crea un endpoint se especifica que tipo de dato tiene que ser 
Automaticamente realiza la validacion

Install 
fastapi
uvicorn


```

uvicorn application:app --reload  

```



## Para correrlo en docker

```

docker build -t fastapi-items .

docker run -d --name fastapi-items -p 80:80 fastapi-items

```



