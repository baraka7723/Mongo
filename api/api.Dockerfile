FROM python:3.9

WORKDIR /app

COPY . .

# Install the requirements
RUN pip install -r requirements.txt

# Expose API port
EXPOSE 6000

CMD [ "python", "app.py" ]
