from fastapi import FastAPI
from pydantic import BaseModel
from model import generate_sql
from db import init_db, execute_sql

app = FastAPI(title="Natural Language → SQL Generator")

class QueryRequest(BaseModel):
    text: str
    execute: bool = False  # Optional: execute SQL after generation

@app.on_event("startup")
def startup():
    init_db()

@app.post("/generate_sql/")
def generate_sql_endpoint(req: QueryRequest):
    sql = generate_sql(req.text)
    result = None
    if req.execute:
        result = execute_sql(sql)
    return {"sql": sql, "result": result}
