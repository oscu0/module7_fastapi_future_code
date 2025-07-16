from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()    # создаём инстанцию FastAPI
templates = Jinja2Templates(directory='templates')

@app.get("/")      # определяем запрос GET для пути "/"
async def root(request):  # определяем функцию (с произвольным именем!), которая обрабатывает этот запрос
    return templates.TemplateResponse(
        name='my_template.html',
        context={
            'request': request,
            'title': 'Самый лучший в мире сайт'})