FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py

# StreamLit port
EXPOSE 8501

CMD ["streamlit", "run", "app.py"]