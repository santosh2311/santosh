FROM python:3.10.8-alpine3.15
WORKDIR /app
COPY /requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000
ENTRYPOINT [ "python","manage.py","runserver","0.0.0:8000" ]