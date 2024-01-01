FROM python:latest
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
