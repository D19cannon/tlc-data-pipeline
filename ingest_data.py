from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
import time
import sys


def main():
    load_dotenv('.env.local')

    user = 'root'
    password = os.environ.get('MYSQL_ROOT_PASSWORD')
    host = os.environ.get('MYSQL_HOST')
    port = os.environ.get('MYSQL_PORT')
    db = os.environ.get('MYSQL_DATABASE')
    table_name = os.environ.get('MYSQL_TABLE_NAME')

    time.sleep(15)

    print(f'mysql+pymysql://{user}:{password}@{host}:{port}/{db}')
    sys.stdout.flush()

    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'
    )
    pd.io.parquet.get_engine('auto')
    print('Reading data...')
    sys.stdout.flush()
    df = pd.read.parquet('./data/2022/january/yellow_tripdata_2022-01.parquet')
    print('Inserting data...')
    sys.stdout.flush()
    df.to_sql(name=table_name, con=engine, if_exists='append')

    __name__ == '__main__'
    main()
