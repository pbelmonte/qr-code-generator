FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./start.sh /code/start.sh
RUN chmod +x /code/start.sh
COPY ./app /code/app
CMD ["./start.sh"]
