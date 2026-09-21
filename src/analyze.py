import pandas as pd

df = pd.read_csv("data/outages.csv", parse_dates=["start_time","end_time"])
df["downtime_hours"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 3600

site = (df.groupby("site_id", as_index=False)
          .agg(outage_count=("outage_id","count"),
               total_downtime_hours=("downtime_hours","sum"),
               mttr_hours=("downtime_hours","mean")))
site["estimated_availability_pct"] = (1 - site["total_downtime_hours"]/(180*24))*100

print(site.sort_values("total_downtime_hours", ascending=False).head(15).to_string(index=False))
