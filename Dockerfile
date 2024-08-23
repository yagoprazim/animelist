FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate
RUN python create_superuser.py

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]