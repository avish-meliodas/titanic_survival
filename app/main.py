from fastapi import FastAPI, BackgroundTasks
from app.schemas import Passenger, PredictionResponse
from app.tasks import async_predict, get_results
from app.model_pred import prediction

app = FastAPI()

@app.post("/titanic_sync", response_model=PredictionResponse)
def titanic_sync(data:Passenger):
    result = prediction([data.model_dump()])[0]
    return result

@app.post("/titanic_async")
def titanic_async(data: Passenger, background_tasks: BackgroundTasks):
    payload = [data.model_dump()]
    job_id = async_predict(payload)
    return {'job_id': job_id}

@app.get("/titanic_async/{job_id}")
def get_async_result(job_id: str):
    result = get_results(job_id)
    if result:
        return result[0]
    return {"status": "processing"}