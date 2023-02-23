from fastapi import APIRouter


app = APIRouter(tags=["{{cookiecutter.app_tag}}"], prefix="/{{cookiecutter.app_prefix}}")


@app.get("/")
async def root():
    return {"message": "Hello World from {{cookiecutter.app_slug}}!"}


