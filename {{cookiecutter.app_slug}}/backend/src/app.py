from fastapi import APIRouter


app = APIRouter(tags=" {{cookiecutter.app_tags}} ", prefix="/{{cookiecutter.app_prefix}}")


