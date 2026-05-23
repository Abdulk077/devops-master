FROM python:3.11-alpine
WORKDIR /app
RUN pip install redis
COPY app.py .
CMD ["python", "app.py"]