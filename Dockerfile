#https://docs.docker.com/language/python/build-images/

FROM python:3.10.0-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
