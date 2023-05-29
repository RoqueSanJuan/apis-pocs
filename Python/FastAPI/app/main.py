# Path es para poder agregar Path argument
# HTTPException y status es para poder inficar un codigo de error
from fastapi import FastAPI, Path, HTTPException, status
# Import Opcinal , es una buena practica

from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


inventory = {
}

@app.get("/")
def get_main():
    return "Ir a /docs para ver el funcionamiento"


# Le digo que el objeto que me tienen que enviar como 
# parametro es un int
# Path me permite hacer una mejor respuesta -> Esto se ve reflejado en el /docs
@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(description="The id of the item")):
    return inventory[item_id]

# Query parameter
# http://127.0.0.1:8000/get-by-name?name=Milk
# Para pasar mas  de 1 parametro se usa el & name=Milk&test=2
# Al agregar el = None lo hago opcional . Buena practica agregar el object Optinal
# Se pueden agrupar los Query arguments y los Path arguments
@app.get("/get-by-name")
def get_item(*, name: Optional[str] = None, test: int):
    for id in inventory:
        if inventory[id].name == name:
            return inventory[id]
    raise HTTPException(status_code=404, detail="El porque del error")

# Creo un item , tengo que definir la clase
# Ejemplo
# curl -X 'POST' \
#   'http://127.0.0.1:8000/create-item/3' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "Egg",
#   "price": 222,
#   "brand": "Huevos"
# }'
@app.post("/create-item/{item_id}")
def create_item(item: Item, item_id:int):
    if item_id in inventory:
        return {"Error": "Item id already exists"}
    
    # inventory[item_id] = {"name":item.name, "brand":item.brand, "price":item.price}
    inventory[item_id] = item

    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item id not exists"}
    
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id:int):
    if item_id not in inventory:
        return {"Error": "Item id not exists"}
    
    del inventory[item_id]
    return {"Eliminado": "Elemento Eliminado"}

# @app.get("/")
# def home():
#     return {"Data":"Test"}

# @app.get("/about")
# def about():
#     return {"Data":"About"}

