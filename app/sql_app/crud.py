from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.SystemInfos).filter(models.SystemInfos.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.SystemInfos).filter(models.SystemInfos.ip_address == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.SysInfo):
    fake_hashed_password = user.ip_address + "notreallyhashed"
    db_user = models.User(email=user.ip_address, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def insert(data: dict):
    db_repo = SystemInfos(
        
    )

    with SessionLocal() as session:
        try:
            session.add(db_repo)
            session.commit()
            session.close()
        except:
            session.rollback()
            session.close()
        else:
            session.commit()
            session.close()