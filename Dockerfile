FROM python:3.12-slim

WORKDIR /app


RUN apt-get update && apt-get install -y curl unzip

COPY requirements.txt  .
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY .  .


EXPOSE 8000

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

CMD [ "reflex", "run" ]  