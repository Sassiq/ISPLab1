FROM python:3.9.1

WORKDIR /app

COPY ./pythonscript.py .

CMD ["python", "pythonscript.py"]
