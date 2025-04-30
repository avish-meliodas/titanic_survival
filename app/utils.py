import pandas as pd
import numpy as np
from app.train import mean_age, median_fare
import pickle

scaler = pickle.load(open('models/scaling.pkl', 'rb'))

def preprocess_data(df):
    ## fill age with mean
    df['Age'].fillna(mean_age, inplace=True)

    ## fill fare with median
    df['Fare'].fillna(median_fare, inplace=True)

    ## remove NULL embarked rows
    df.dropna(subset=['Embarked'], inplace=True)
    if(df.shape[0] ==0 ):
        return pd.DataFrame()

    ## create num_cabins from Cabin
    df['num_cabin'] = df['Cabin'].apply(lambda x: 0 if pd.isna(x) else len(x.split(' ')))

    ## create cabin_letter from Cabin
    df['cabin_letter'] = df['Cabin'].apply(lambda x: 'n' if pd.isna(x)==True else str(x)[0])

    ## create name_tag from Name
    df['name_tag'] = df['Name'].apply(lambda x: x.split(' ')[1] )

    ## Pclass to str
    df['Pclass'] = df['Pclass'].astype(str)

    ## make norm = log(x+1) for fare column
    df['norm_fare'] = np.log( df['Fare'] + 1 )

    ## scaling for Age an norm_fare
    df[['Age', 'norm_fare']] = scaler.transform( df[['Age', 'norm_fare']] )
    
    ## convert categrical columns to 'category' type
    # Find all object columns
    cat_cols = ['Pclass', 'Sex', 'Embarked', 'cabin_letter', 'name_tag']

    for col in cat_cols:
        df[col] = df[col].astype('category')

    processed_df = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Embarked',
                        'num_cabin', 'cabin_letter', 'name_tag', 'norm_fare']]
    
    return processed_df
