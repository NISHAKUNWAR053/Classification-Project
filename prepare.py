import pandas as pd
import numpy as np
import env
import os

from pydataset import data
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def clean_telco(df):
    to_drop = ['Unnamed: 0', 'customer_id', 'contract_type_id.1', 'paperless_billing.1',
                   'gender.1', 'senior_citizen.1', 'partner.1', 'dependents.1', 
                   'payment_type_id.1', 'monthly_charges.1', 'total_charges.1', 'signup_date']
    df.drop(columns = to_drop, inplace = True)
    df.drop(df.columns[0], axis = 1, inplace = True)
    df ['total_charges'] = (df.tenure * df.monthly_charges)
    df = df[df.total_charges != 0]
    df['charge_rank'] = pd.qcut(df['total_charges'], 4, labels = ['a','b','c','d'])
    return df


def dummies_telco(df):
    '''
    this function generates dummy columns for modeling
    '''
    outout = []
    outout = pd.get_dummies(df[['charge_rank', 'internet_service_type', 'gender', 'senior_citizen', 'partner', 
                                                'contract_type', 'dependents', 'phone_service','multiple_lines',
                                               'online_security', 'online_backup','device_protection','streaming_tv', 
                                                'paperless_billing','churn', 'contract_type','internet_service_type',
                                               'payment_type']],drop_first = [True, True])
    outout['customer_id'] = df.customer_id
    return outout


def train_val_test(df, target):
    '''
    this function splits up the data into sections for training,
    validating, and testing
    models
    '''
    seed = 99
    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed, stratify = df[target])
    validate, test = train_test_split(val_test, train_size = 0.5, random_state = seed,
                                      stratify = val_test[target])
    return train, validate, test