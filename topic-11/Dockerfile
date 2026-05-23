FROM python:3.11-alpine
WORKDIR /app
COPY app.py .
HEALTHCHECK --interval=5s --timeout=3s --retries=3 --start-period=15s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1
CMD ["python", "app.py"]