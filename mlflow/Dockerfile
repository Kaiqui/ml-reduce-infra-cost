FROM python:3.9-slim-buster

ARG DB_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

RUN pip install mlflow boto3 pymysql

ENV DB_URL=$DB_URL \
    AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

WORKDIR /app

COPY entrypoint.sh /app

RUN chmod +x /app/entrypoint.sh

RUN ./app/entrypoint.sh

CMD ["mlflow", "server", "--port", "8081","--host", "0.0.0.0", "--backend-store-uri", "${DB_URL}","--default-artifact-root","s3://s3_bucket_name"]
EXPOSE 8081