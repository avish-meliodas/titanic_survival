from uuid import uuid4

results = {}

def async_predict(data):
    from app.model_pred import prediction
    job_id = str(uuid4())

    result = prediction(data)

    results[job_id] = result

    return job_id

def get_results(job_id):
    
    return results.get(job_id)