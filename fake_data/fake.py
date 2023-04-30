import numpy as np
import pandas as pd

num_servers = 100000
cpu_load_range = (0.0, 100.0)
cpu_cores_range = (1, 32)
memory_ram_range = (0.0, 100.0)
memory_swap_range = (0.0, 100.0)
disk_usage_range = (0.0, 100.0)

cpu_load = np.random.uniform(cpu_load_range[0], cpu_load_range[1], size=num_servers)
cpu_cores = np.random.randint(cpu_cores_range[0], cpu_cores_range[1] + 1, size=num_servers)
memory_ram = np.random.uniform(memory_ram_range[0], memory_ram_range[1], size=num_servers)
memory_swap = np.random.uniform(memory_swap_range[0], memory_swap_range[1], size=num_servers)
disk_usage = np.random.uniform(disk_usage_range[0], disk_usage_range[1], size=num_servers)

df = pd.DataFrame({'CPU Load (%)': cpu_load,
                   'CPU Cores': cpu_cores,
                   'Memory RAM Usage (%)': memory_ram,
                   'Memory Swap Usage (%)': memory_swap,
                   'Disk Usage (%)': disk_usage})

df['Downgrade'] = ((df['CPU Load (%)'] > 70.0) | (df['Memory Swap Usage (%)'] > 50.0) | (df['CPU Cores'] > 16) | ((df['Memory RAM Usage (%)'] + df['Memory Swap Usage (%)']) > 70.0) | (df['Disk Usage (%)'] > 80.0))

print(df.head())
