""" FastAPI Main entrypoint """


from fastapi import FastAPI, HTTPException, status, Query, Body
from pydantic import BaseModel, Field
from typing import Annotated, Union
from models import Video

from services import (
    APIService,
    ItemNotFoundError,
)
from fastapi.responses import PlainTextResponse, RedirectResponse
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sonic Sampling APIService",
    contact={
        "name" :"Elijah Wood",
        "url" :"",
    },
    description="An API designed to retrieve random YouTube URL's to sample and download",
    openapi_tags=[],
)

services = APIService()

# Add CORS middleware
# TODO: make CORS permissions secure
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


