from pydantic import (
    BaseModel,
    Field
)


class SysInfo(BaseModel):
    # Host
    hostname: str = Field()
    ip_address: str = Field()

    # CPU
    cpu_percent: float = Field()
    cpu_load: float = Field()
    cpu_core: int = Field()

    # Memory
    virtual_memory_percent: float = Field()
    swap_memory_percent: float = Field()

    # Network
    bytes_sent: float = Field()
    bytes_sent_unit: str = Field()

    bytes_recv: float = Field()
    bytes_recv_unit: str = Field()

    packets_sent: float = Field()
    packets_sent_unit: str = Field()

    packets_recv: float = Field()
    packets_recv_unit: str = Field()

    # Disk
    disk_used_percent: float = Field()
    read_count: float = Field()
    write_count: float = Field()
    read_count_unit: str = Field()
    write_count_unit: str = Field()