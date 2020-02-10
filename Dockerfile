FROM python:3.7-stretch

COPY meme app
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt

RUN ["python", "manage.py", "makemigrations", "hookah"]
RUN ["python", "manage.py", "migrate"]

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]