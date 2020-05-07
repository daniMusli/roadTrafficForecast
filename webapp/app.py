import flask
from tensorflow.keras.models import load_model
import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])

def main():
    df = pd.read_csv("./data/test.csv", encoding='utf-8')
    scaler = MinMaxScaler(feature_range=(0, 1)).fit(df['Flow (Veh/5 Minutes)'].values.reshape(-1, 1))
    test_data = scaler.transform(df['Flow (Veh/5 Minutes)'].values.reshape(-1, 1)).reshape(1, -1)[0]
    lag = 12
    test = []
    for i in range(lag, len(test_data)):
        test.append(test_data[i - lag: i + 1])
    test = np.array(test)
    x_test = test[:, :-1]
    y_test = test[:, -1]
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    print("Loading LSTM keras model...")
    model_lstm = load_model('./models/LSTM.h5') 
    print("LSTM model successfully loaded") 
    print("Loading GRU keras model...")
    model_GRU = load_model('./models/GRU.h5') 
    print("GRU model successfully loaded")    
    predicted_lstm = model_lstm.predict(x_test)    
    predicted_lstm = scaler.inverse_transform(predicted_lstm.reshape(-1, 1)).reshape(1, -1)[0]    
    predicted_GRU = model_GRU.predict(x_test)    
    predicted_GRU = scaler.inverse_transform(predicted_GRU.reshape(-1, 1)).reshape(1, -1)[0]    
    if flask.request.method == 'GET':
        return(flask.render_template('index.html')) 
    if flask.request.method == 'POST':
        date = flask.request.form['date']
        time = flask.request.form['time']
        col = date + " " + time 
        x=df.loc[df['5 Minutes'] ==col] 
        true = x["Flow (Veh/5 Minutes)"].values
        t_value = np.asscalar(true)
        index = x["Flow (Veh/5 Minutes)"].index
        index = index[0]
        pred_LSTM = predicted_lstm[index].astype(int) 
        pred_GRU = predicted_GRU[index].astype(int) 
        return flask.render_template('index.html',true_val=true,pred_val_LSTM=pred_LSTM,pred_val_GRU=pred_GRU)

        
if __name__ == '__main__':
   
    app.run()
    
