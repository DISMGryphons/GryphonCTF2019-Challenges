FROM ubuntu:latest
RUN apt update && apt upgrade -y
RUN apt install -y python3 python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
COPY . /app
WORKDIR /app/
RUN rm /app/requirements.txt \
    rm /app/Dockerfile
RUN useradd -M pew
RUN chown -R pew:pew /app
USER pew
CMD ["gunicorn", "--threads", "8", "-b", "0.0.0.0:8000", "routes:app"]