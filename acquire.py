import pandas as pd
import numpy as np
from env import get_connection
import csv
import os


def get_telco_data(df):
    filename = 'telco.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql(''' SELECT *
                             FROM customers
                             JOIN cotract_types USING (contract_type_id)
                             JOIN internet_service_types USING (internet_service_type_id)
                             JOIN customer_subscriptions USING (customer_id)
                             JOIN customer_payments USING (customer_id)
                             JOIN customer_contracts USING (customer_id)
                             JOIN customer_signups USING (customer_id)''',
                         url = get_connection('telco_churn'))
                         # read the sql query into a dataframe 

        df.to_csv(filename, index = False) # write the dataframe to disk for later.

        return df # returned tha dataframe to the calling code



def telco_data_acquire(telco_df):
    print(telco_df.info())
    print('               ')
    print(telco_df.describe())
    print('               ')
    print(telco_df.describe(include = 'object').T)
    print('               ')
    print('The telco data used for this project has', telco_df.shape[0], 'rows and', telco_df.shape[1], 'columnc')
    print('               ')
    print('This was the initial exploratio of acquired data')
    return telco_df


