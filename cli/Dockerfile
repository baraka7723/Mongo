FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the container
COPY mongo_cli.py .

# Install the required packages
RUN pip install requests

# Run the Python script when the container starts
CMD [ "python", "mongo_cli.py" ]

