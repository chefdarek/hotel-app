FROM python:3.9 

WORKDIR /hotel-app

COPY . /hotel-app


RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["python", "hotel-app/main.py"]