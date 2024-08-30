FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/media/anime_images

RUN python manage.py migrate
RUN python create_superuser.py
RUN python load_initial_data.py

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]