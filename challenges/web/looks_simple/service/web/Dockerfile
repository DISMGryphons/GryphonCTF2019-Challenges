FROM ubuntu:latest
RUN apt update && apt upgrade -y
RUN apt install -y python3 python3-pip
COPY . /app
WORKDIR /app/
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
CMD ["gunicorn", "-w", "4", "routes:app"]