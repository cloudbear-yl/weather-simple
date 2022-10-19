FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080

# ADD final_app.py .
CMD [ "python", "./final_app.py" ]



