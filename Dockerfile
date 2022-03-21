FROM python:3.8-slim-buster
COPY ./webapp/*.py /webapp/
COPY app.py /
WORKDIR /
ENV PYTHONBUFFERED 1
RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python3", "app.py"]
