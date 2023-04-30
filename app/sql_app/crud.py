from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas


def get_sys_info(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SystemInfos).offset(skip).limit(limit).all()


def create_user(db: Session, server: schemas.SysInfo):
    current_dateTime = datetime.now()
    db_user = models.SystemInfos(
        date_created=current_dateTime,
        hostname=server.hostname,
        ip_address=server.ip_address,
        cpu_percent=server.cpu_percent,
        cpu_load=server.cpu_load,
        cpu_core=server.cpu_core,
        virtual_memory_percent=server.virtual_memory_percent,
        swap_memory_percent=server.swap_memory_percent,
        disk_used_percent=server.disk_used_percent
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
