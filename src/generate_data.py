from pathlib import Path
import random
from datetime import datetime, timedelta
import pandas as pd

random.seed(42)
rows = []
start = datetime(2026,1,1)
for i in range(800):
    opened = start + timedelta(hours=random.randint(0, 24*180))
    duration = max(0.2, random.gammavariate(2.0, 1.5))
    rows.append({
        "outage_id": f"O{i+1:04d}",
        "site_id": f"S{random.randint(1,120):04d}",
        "circle": random.choice(["NORTH","WEST","SOUTH","EAST"]),
        "start_time": opened,
        "end_time": opened + timedelta(hours=duration),
        "cause": random.choice(["POWER","TRANSMISSION","HARDWARE","BATTERY","UNKNOWN"])
    })

Path("data").mkdir(exist_ok=True)
pd.DataFrame(rows).to_csv("data/outages.csv", index=False)
print("Synthetic outage dataset created.")
