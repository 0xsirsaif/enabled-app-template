from fastapi import APIRouter
from fastapi.responses import RedirectResponse


app = APIRouter(tags=["{{cookiecutter.app_tag}}"], prefix="/{{cookiecutter.app_prefix}}")


@app.get("/")
async def read_root():
    return RedirectResponse(url="http://127.0.0.1:8000/{{cookiecutter.app_slug}}/frontend/out/index.html")

