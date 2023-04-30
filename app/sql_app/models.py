from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Sequence
)

from .database import Base


class SystemInfos(Base):
    __tablename__ = "system_infos"
    id = Column('id', Integer, Sequence('id', start=0), primary_key=True)
    date_created = Column(DateTime)

    hostname = Column(String(255))
    ip_address = Column(String(100))

    cpu_percent = Column('cpu_percent', Float)
    cpu_load = Column('cpu_load', Float)
    cpu_core = Column('cpu_core', Integer)

    # Memory
    virtual_memory_percent = Column('virtual_memory_percent', Float)
    swap_memory_percent = Column('swap_memory_percent', Float)

    # Disk
    disk_used_percent = Column('disk_usage_percent', Float)
