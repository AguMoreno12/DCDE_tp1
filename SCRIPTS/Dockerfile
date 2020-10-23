# Dockerfile
# Use an official Python runtime as a parent image
FROM debian:10.3-slim

# Set the working directory to /app
# in the container
WORKDIR /usr/src/myapp

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get -y dist-upgrade

RUN apt-get -y install apt-utils \
    build-essential \
    python3 \
    gcc \
    python3-dev \
    python3-pip \
    python3-numpy \
    python3-pandas \
    default-mysql-client

COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Run app.py when the container launches
# The -u flag specifies to use the unbuffered ouput.
# in this way, what's printed by the app is visible on the host
# while the container is running
# CMD ["python3", "-u", "scriptpy.py"]