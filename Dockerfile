FROM python

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /django
RUN mkdir -p /var/lib/mysql/
WORKDIR /django
COPY . .
RUN pip install -r requirements.txt
# EXPOSE 80
RUN python manage.py makemigrations
# CMD python manage.py runserver 0.0.0.0:80