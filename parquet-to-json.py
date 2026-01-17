import pandas as pd

df = pd.read_parquet("dpwh_transparency_data.parquet")

df.to_json("dpwh_transparency_data.json", orient="records", indent=2)