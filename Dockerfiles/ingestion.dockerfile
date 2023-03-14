FROM python:3.9.1

RUN pip3 install pandas sqlalchemy psycopg2 python-dotenv pymysql cryptography pyarrow fastparquet

WORKDIR /app
COPY ./data data

ENTRYPOINT ["python"]
CMD ["./scripts/ingest_data.py"]

