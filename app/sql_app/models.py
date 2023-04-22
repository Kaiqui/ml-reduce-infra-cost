from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    Sequence
)

from .database import Base


class SystemInfos(Base):
    __tablename__ = "system_infos"
    id = Column('id', Integer, Sequence('id', start=0), primary_key=True)
    date_created = Column(Date)

    hostname = Column(String(255))
    ip_address = Column(String(100))

    cpu_percent = Column('cpu_percent', Float)
    cpu_load = Column('cpu_load', Float)
    cpu_core = Column('cpu_core', Integer)

    # Memory
    virtual_memory_percent = Column('virtual_memory_percent', Float)
    swap_memory_percent = Column('swap_memory_percent', Float)

    # Network
    # enviados: TX recebidos: RX
    bytes_sent = Column('bytes_sent', Float)
    bytes_sent_unit = Column('bytes_sent_unit', String(5))

    bytes_recv = Column('bytes_recv', Float)
    bytes_recv_unit = Column('bytes_recv_unit', String(5))

    packets_sent = Column('packets_sent', Float)
    packets_sent_unit = Column('packets_sent_unit', String(5))

    packets_recv = Column('packets_recv', Float)
    packets_recv_unit = Column('packets_recv_unit', String(5))

    # Disk
    disk_used_percent = Column('disk_usage_percent', Float)
    read_count = Column('read_count', Float)
    write_count = Column('write_count', Float)
    read_count_unit = Column('read_count_unit', String(5))
    write_count_unit = Column('write_count_unit', String(5))
