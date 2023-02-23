from fastapi import APIRouter


app = APIRouter(tags=["{{cookiecutter.app_tag}}"], prefix="/{{cookiecutter.app_prefix}}")


