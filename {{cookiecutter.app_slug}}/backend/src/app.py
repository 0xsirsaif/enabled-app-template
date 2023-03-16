from fastapi import APIRouter
from fastapi.responses import FileResponse


app = APIRouter(tags=["{{cookiecutter.app_tag}}"], prefix="/{{cookiecutter.app_prefix}}")


@app.get("/")
async def read_root():
    return FileResponse("{{cookiecutter.app_slug}}/frontend/build/index.html")

