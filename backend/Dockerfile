FROM python:3.10

COPY ./ /app/

WORKDIR /app

ENV FLASK_APP "./app/app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

WORKDIR /app

CMD ["python", "app.py"]