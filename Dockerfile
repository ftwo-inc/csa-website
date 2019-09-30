FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt


COPY .secrets /code/.env

COPY . /code/

# Expose port
EXPOSE 8080

RUN ["python", "manage.py", "collectstatic"]

ENTRYPOINT ["bash", "./entrypoint.sh"]
