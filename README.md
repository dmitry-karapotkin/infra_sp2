# API проекта Yamdb
### Описание
Программно-ориентированный интерфейс ресурса а-ля Кинопоиск
### Технологии
Docker
язык Python 3.8.5
фреймворк Django 3.0.5
### Запуск проекта
- установите Docker (https://docs.docker.com/get-started/)
- введите в терминале команду "git clone https://github.com/dmitry-karapotkin/infra_sp2.git"
- укажите в файле .env параметры доступа к базе данных, используемый движок, а также переменные, чувствительные с точки зрения безопасности
- введите в коммандной строке в папке расположения проекта друг за другом следующие команды:
docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
- зайдите на страницу администрирования проекта, введя в браузере 127.0.0.1:8000/admin или localhost/admin
- заполните базу данных тестовыми записями
- попробуйте запустить тесты: docker-compose exec web pytest
- остановите работу контейнеров: docker-compose stop
- удалите контейнеры командой: docker-compose down
### Авторы
Димон, которому лень писать подробные инструкции