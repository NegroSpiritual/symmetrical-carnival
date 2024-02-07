from fastapi import FastAPI
from routers import user, auth
app = FastAPI(
    title='Liver Disease Detection'
)
