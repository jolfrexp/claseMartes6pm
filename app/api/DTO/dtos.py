from pydantic import BaseModel,Field
from datetime import date 

#los DTO son clases que establecen
#el modelo de trasnferencia de datos

class UsuarioDTOPeticion(BaseModel):
    nombres : str
    edad : int
    telefono: str
    correo : str
    contraseña : str
    fechaRegistro : date
    ciudad : str
    class Config:   # trae la informacion de la BD
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id : int
    nombres : str
    correo : str
    fechaRegistro: date
    class Config:   
        orm_mode=True


# gastoDTOPeticion
class gastoDTOPeticion(BaseModel):
    monto : int
    fecha : date
    descripcion : str
    nombre : str
    class Config:
        orm_mode=True
class gastoDTORespuesta(BaseModel):
    idGasto : int
    monto : int
    fecha : date
    descripcion : str
    nombre : str
    class Config:
        orm_mode=True

# CategoriaDTOPeticion
class CategoriaDTOPeticion:
    idCategoria : int
    nombreCategoria : str
    descripcion : str
    fotoicono : str
    class Config:
        orm_mode=True

class CategoriaDTORespuesta:
    idCategoria : int
    nombreCategoria : str
    descripcion : str
    fotoicono : str
    class Config:
        orm_mode=True
# IngresoDTOPeticion

class IngresoDTOPeticion:
    idIngresos: int
    nombreMetodo: str
    descripcion: str
    class Config:
        orm_mode=True
class IngresoDTORespuesta:
    idIngresos: int
    nombreMetodo: str
    descripcion: str
    class Config:
        orm_mode=True

# FacturaDTOPeticion
class FacturaDTORespuesta(BaseModel):
    idFactura: str
    fecha : date
    usuario : str
    metodo : str
    gasto : str
    subtotal : float
    total : float
    class Config:
        orm_mode=True
class FacturaDTOPeticion(BaseModel):
    fecha : date
    usuario_id : int
    metodo_id : int
    categoria_id : int
    gasto_id : int
    subtotal  :  float
    total  : float
    class Config:
        orm_mode=True