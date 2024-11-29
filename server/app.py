from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import joblib
from sklearn.datasets import load_iris

class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Load the pretrained model
model = joblib.load('model.pkl')

#Instance FastAPI
app = FastAPI()

@app.post("/predict")
def predict(item: Item):

    item_data = jsonable_encoder(item)

    sepal_length = float(item_data["sepal_length"])
    sepal_width = float(item_data["sepal_width"])
    petal_length = float(item_data["petal_length"])
    petal_width = float(item_data["petal_width"])
    
    #Prédiction en utilisant le modèle
    prediction = model.predict([[sepal_length,sepal_width,petal_length,petal_width]] )

    data = load_iris()
    #Retourne la prédiction
    return {"prediction": data.target_names[int(prediction[0])]}