# generate docker file for scrapy
FROM python:3.10.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# cd to crawler directory
WORKDIR /app/crawler

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /app/entry.sh

ENTRYPOINT [ "/app/entry.sh" ]
