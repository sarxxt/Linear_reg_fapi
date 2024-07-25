import uvicorn 
from fastapi import FastAPI
from data_notes import DataNote
import pickle
import numpy as np
from sklearn.model_selection import train_test_split


#createing app object
app = FastAPI()
pickle_in = open("model.pkl", "rb")
regression_model =pickle.load(pickle_in)

@app.post('/predict')
def predict_sepal_length(data:DataNote):
    data = data.model_dump()
   # data = json.loads(data)
    print(data,type(data))
    petal_length = data['petal_length']
    prediction = regression_model.predict(np.array([[petal_length]]))
    # Print the prediction
    print(f"Predicted sepal length for petal length {petal_length}: {prediction[0]}")
    return f"Predicted sepal length for petal length {petal_length}: {prediction[0]}"

if __name__ == '__main__':
    uvicorn.run(app, host ='127.0.0.1',  port =8000)

