FROM python:3

COPY . .
RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-b=:80", "--access-logfile=-", "main:app"]
