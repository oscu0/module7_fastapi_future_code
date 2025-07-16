from jinja2 import Environment, FileSystemLoader          # подключение шаблонизатора
env = Environment(loader=FileSystemLoader("."))   # создание ему окружения
template = env.get_template("my_template.html")               # чтение шаблона
html_output = template.render(title="Лучший в мире сайт") # передача данных
print(html_output)