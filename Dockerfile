FROM python:3.9-slim
RUN pip install requests
COPY app.py app.py
CMD ["python", "app.py"]
