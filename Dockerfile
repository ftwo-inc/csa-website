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

# RUN ["python", "manage.py", "collectstatic", "--no-input"]
# This is too slow to be done on GCB. Manual for now.

ENTRYPOINT ["bash", "./entrypoint.sh"]
