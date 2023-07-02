import io
import os
import pandas as pd
import numpy as np
import pickle
import tarfile
import subprocess

subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

from catboost import CatBoostClassifier
        
def input_fn(input_data, content_type):
    if content_type == "text/csv":
        s = io.StringIO(input_data)
        data = pd.read_csv(s, header=None)
        data = data.iloc[:, 1:]
        data.columns = [f"feature_{x}" for x in range(data.shape[1])]
        print(data)
        return data
    else:
        raise ValueError("{} not supported by script!".format(content_type))
        
def model_fn(model_dir):
    file_path = os.path.join(model_dir, "model")
    model = CatBoostClassifier()
    model.load_model(file_path)
    return model

def predict_fn(input_data, model):
    model_output = model.predict(input_data, prediction_type="Probability")
    predicted_label = np.argmax(model_output, axis=1)
    return predicted_label

def output_fn(prediction, content_type):
    print(prediction)
    res = int(prediction[0])
    return res