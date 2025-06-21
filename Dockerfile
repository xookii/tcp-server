FROM python:3.11-slim

WORKDIR /app
COPY tcp_server.py .

CMD ["python", "server.py"]
