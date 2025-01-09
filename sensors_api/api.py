#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring. missing-function-docstring, missing-class-docstring

import logging

from datetime import datetime
from typing import List, Optional

import uvicorn

from decouple import config
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import APIKeyHeader
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import field_validator


ALL_GOOD = {"message": "OK."}
DB_FILE_NAME = 'sensors.sqlite'
X_API_KEY = config('X_API_KEY')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

header_scheme = APIKeyHeader(name="X-API-Key")

class SensorsData(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    readtime: Optional[datetime] = Field(default_factory=lambda: datetime.now())
    regname: str = Field(index=True)
    value: str | None = None
    dt: datetime | None = None

    @field_validator('dt', mode='after')
    def validate_dt(cls, value): # pylint: disable=no-self-argument
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        return value


engine = create_engine(f"sqlite:///{DB_FILE_NAME}")
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()


@app.post("/sensors")
def add_data(data: SensorsData, session: Session = Depends(get_session), api_key: str = Depends(header_scheme)):
    if api_key != X_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    try:
        print(data)
        asd = SensorsData.model_validate(data)
        session.add(asd)
        session.commit()

    except Exception as e:
        logger.exception("Error adding data.")
        raise HTTPException(status_code=500, detail="Internal error.") from e

    return ALL_GOOD


@app.get("/sensors", response_model=List[SensorsData])
def read_data(session: Session = Depends(get_session), api_key: str = Depends(header_scheme)):
    if api_key != X_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    data = session.exec(select(SensorsData).order_by(SensorsData.readtime.desc()).limit(10)) # pylint disable=no-member
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
