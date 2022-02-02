# Set base image (host OS)
FROM python:3.8-alpine
# Set the working directory in the container
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
#command to run on container start
CMD [ "python", "./app.py" ]