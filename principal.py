from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para recibir datos
class Datos(BaseModel):
    parametro: int

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta principal
@app.get("/")
async def root():
    return FileResponse("static/principal.html")

# Ruta home
@app.get("/Home")
async def root():
    return FileResponse("static/Home.html")













# Endpoint que recibe el parámetro 2
@app.post("/")
async def recibir_datos(datos: Datos):
    print(f"Parámetro recibido: {datos.parametro}")
    return {"status": "success", "parametro_recibido": datos.parametro}
