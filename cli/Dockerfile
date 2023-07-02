FROM python:3.9

WORKDIR /app

COPY mongo_cli.py .

RUN pip install requests

CMD [ "python", "mongo_cli.py" ]

