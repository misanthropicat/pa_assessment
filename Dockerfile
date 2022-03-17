FROM python:3.8-slim-buster
WORKDIR /
ENV PYTHONBUFFERED 1
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./webapp/*.py /webapp
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["-m", "webapp.main"]
