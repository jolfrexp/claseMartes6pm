from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends 
from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta,gastoDTORespuesta,gastoDTOPeticion
from app.api.models.tablassql import Usuario,Gasto
from app.database.configuration import sessionLocal, engine

rutas=APIRouter()

def conectarConBd():
    baseDatos=sessionLocal()  #crear el camino de conexion con la bd
    try:
        yield baseDatos
    except Exception as error:
        baseDatos.rollback()  # parar todas las peticiones
        raise error #cuenta que paso (el error)

    finally:
        baseDatos.close()  #cerrar peticion  

    
#   construyendo nuestros servicios

#Cada servicio (operacion o transaccion en BD) debe programarse como una funcion
@rutas.post("/usuario", response_model=UsuarioDTORespuesta, summary="Registrar un usuario en la base de datos") #documentando un servicio 
def guardarUsuario(datosUsuario:UsuarioDTOPeticion,database:Session=Depends(conectarConBd)): # con esto podemos comunicarme con la base de datos
    # debemos filtrar los datos, para que coincidan con la base de datos
    try:
        usuario=Usuario(
            nombres=datosUsuario.nombres,
            edad = datosUsuario.edad,
            telefono=datosUsuario.telefono,
            correo=datosUsuario.correo,
            contraseña=datosUsuario.contraseña,
            fechaRegistro = datosUsuario.fechaRegistro,
            ciudad=datosUsuario.ciudad

        )
        #ordenando a la base de datos
        database.add(usuario) #agregemelo
        database.commit()#tomele foto 
        database.refresh(usuario) #refresquelo
        return usuario  #devuelvamelo

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
@rutas.get("/usuario",response_model=list[UsuarioDTORespuesta],summary="Buscar todos los usuarios en BD")
def buscarUsuarios(database:Session=Depends(conectarConBd)):
    try:
        usuarios = database.query(Usuario).all()
        return usuarios

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")

@rutas.post("/gasto", response_model=gastoDTORespuesta, summary="Registrar un gasto en la base de datos") #documentando un servicio 
def guardarGasto(datosGasto:gastoDTOPeticion,database:Session=Depends(conectarConBd)): # con esto podemos comunicarme con la base de datos
    # debemos filtrar los datos, para que coincidan con la base de datos
    try:
        gasto=Gasto(
            monto=datosGasto.monto,
            fecha=datosGasto.fecha,
            descripcion= datosGasto.descripcion,
            nombre=datosGasto.nombre
        )
        #ordenando a la base de datos
        database.add(gasto) #agregemelo
        database.commit()#tomele foto 
        database.refresh(gasto) #refresquelo
        return gasto  #devuelvamelo

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
@rutas.get("/gasto",response_model=list[gastoDTORespuesta],summary="Buscar todos los gastos en BD")
def buscarGasto(database:Session=Depends(conectarConBd)):
    try:
        gastos = database.query(Gasto).all()
        return gastos

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
#Tarea hacer Gasto