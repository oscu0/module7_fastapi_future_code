from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()    # создаём инстанцию FastAPI
templates = Jinja2Templates(directory='templates')

@app.get("/")      # определяем запрос GET для пути "/"
async def root(request: Request):  # Домашняя страница
    return templates.TemplateResponse(
        name='my_template.html',
        context={
            'request': request,
            'title': 'Самый лучший в мире сайт'})
            
            
@app.get("/profile")      # определяем запрос GET для пути "/profile"
async def profile(request: Request):  # пользователь
    return templates.TemplateResponse(
        name='user.html',
        context={
            'request': request,
            'user': {'is_admin': True},
            'title': 'Страница пользователя'
        })

@app.get("/users")      # определяем запрос GET для пути "/users"
async def all_users(request: Request):  # пользователи
    return templates.TemplateResponse(
        name='users.html',
        context={
            'request': request,
            'items': ['Alisa', 'Bob']})
