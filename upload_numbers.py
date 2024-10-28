import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('/opt/list.csv', names=['phone_number'], header=0)
engine = create_engine('mysql+pymysql://freeswitch:freeswitch@127.0.0.1:3306/caller_id_list')

df.to_sql('caller_id_list', con=engine, if_exists='append', index=False)
