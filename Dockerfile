FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install flask gunicorn numpy pandas

EXPOSE 10000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]