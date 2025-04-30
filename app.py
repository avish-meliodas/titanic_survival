import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, app, jsonify, url_for, render_template
from app.utils import preprocess_data


app = Flask(__name__)

lgbm_model = pickle.load(open('models/LGB_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    # print('DATA is here')
    # print(data)
    # print('TYPE OF DATA IS :', type(data))
    # single_row_data = (np.array(list(data.values())).reshape(1,-1))
    df = pd.DataFrame(data, index=[0])

    ## do data cleaning and transformation
    # column_transformations
    ## do scaling for age and norm_dare columns
    # scaler.transform...
    new_data = preprocess_data(df)
    if(new_data.shape[0] == 0):
        return "No DATA FOUND, maybe Embarked was empty"

    output = lgbm_model.predict(new_data)

    ans = float(output[0] > 0.5)
    ## 1 /0 prediction
    ## return the output
    print('the case is ', ans, ' with probability : ', output[0]*100 )

    return jsonify(ans)

if __name__=="__main__":
    app.run(debug=True)


