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

    # Disk
    disk_used_percent: float = Field()