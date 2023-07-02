FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the source code to the container
COPY . .

# Install the required packages
RUN pip install -r requirements.txt

# Expose the API port
EXPOSE 6000

# Run the API when the container starts
CMD [ "python", "app.py" ]
