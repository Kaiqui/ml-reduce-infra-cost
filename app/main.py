from fastapi import Depends, FastAPI, HTTPException
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from sql_app import crud, models, schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/infra/", response_model=schemas.SysInfo)
def create_user(user: schemas.SysInfo, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.hostname)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)