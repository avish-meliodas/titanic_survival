from pydantic import BaseModel
from typing import List

class Passenger(BaseModel):
    PassengerId : str
    Pclass : str
    Name : str
    Sex : str
    Age : int
    SibSp : int
    Parch : int
    Ticket : str
    Fare : float
    Cabin: str
    Embarked : str

class PredictionResponse(BaseModel):
    survived: int
    probability: float
    