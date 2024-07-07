FROM python:3.9

WORKDIR /app

COPY . /app

RUN mkdir /app/log/
RUN apt update && apt install -y libgl1-mesa-glx poppler-utils tesseract-ocr-por
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]
