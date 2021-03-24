FROM python:3.9 

WORKDIR /

COPY . /


RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]