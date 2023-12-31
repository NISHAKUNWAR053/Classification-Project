import pandas as pd
import numpy as np
import acquire
from env import get_connection
import os

#from pydataset import data
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def prep_telco(df):
    df_telco = acquire.get_telco_data(df)
    df_telco.drop(columns=['internet_service_type_id', 'payment_type_id'], inplace=True) 
    dummy_df_telco = pd.get_dummies(df_telco[['partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'internet_service_type', 'gender']], dummy_na=False, drop_first=True, dtype = int)
    
    ct_df = pd.DataFrame({'contract_type': df_telco['contract_type']})
    ct_df['contract_type_Yes'] = ct_df['contract_type'].apply(lambda x: 0 if x == 'Month-to-month' else 1)
    
    df_telco = pd.concat([df_telco, dummy_df_telco, ct_df], axis=1)
    df_telco.drop(columns=['partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'internet_service_type', 'gender', 'contract_type_id'], inplace=True)  
    df_telco.total_charges = df_telco.total_charges.str.replace(' ', '0').astype('float')  
    return df_telco

def split_telco(df):
    df_telco = prep_telco(df)
    train, telco_test = train_test_split(df_telco, test_size=0.2, random_state=123)
    telco_train, telco_validate = train_test_split(train, test_size=0.25, random_state=123)   
    return telco_train, telco_validate, telco_test


