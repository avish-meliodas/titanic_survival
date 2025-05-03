import pickle
from app.utils import preprocess_data
import pandas as pd

lgbm_model = pickle.load(open('models/LGB_model.pkl', 'rb'))

def prediction(data : list):
    
    df = pd.DataFrame(data[0], index=[0])
    new_data = preprocess_data(df)
    if(new_data.shape[0] == 0):
        return "No DATA FOUND, maybe Embarked was empty"
    
    output = lgbm_model.predict(new_data)
    ans = float(output[0] > 0.5)

    return [{
        "survived": int(ans),
        "probability": output[0]
    }]