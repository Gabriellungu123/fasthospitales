# Lo que tiene que tener 
from typing import Union
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#Para añadir la carpeta data
from data.modelo.menu import Menu
from data.dao.dao_hospitales import Daohospitales
from typing import Annotated
from data.database import database
#Para que funcione el Fastapi los css y los html
app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="templates")



#Primera pagina
@app.get("/")
def get_hospital(request: Request):
    menu = Menu(True, True)
    hospitales = Daohospitales().get_all(database)
    return templates.TemplateResponse(
        request=request,
        name="default.html",
        context={"menu": menu, "hospitales": hospitales})
    
#Ver pagina 

# Insertar pagina
#Eliminar pagina
#Actualizar Pagina