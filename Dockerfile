FROM python:3.8-rc-slim

WORKDIR /app
COPY . .

RUN pip install -r /app/requirements.txt
CMD ["python","app.py"]


