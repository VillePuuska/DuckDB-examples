import json
import pandas as pd
import numpy as np
import random
from datetime import datetime
import os

# If data/ directory is missing, create it.
os.makedirs("data", exist_ok=True)

# Optional fields and tags for generated records.
optional_fields = ["col1", "col2", "col3"]
optional_tags = ["a", "b", "c", "d"]

# Start and end timestamp for randomly generated timestamps.
start_timestamp = round(datetime.fromisoformat("2023-01-01 00:00:00").timestamp())
end_timestamp = round(datetime.fromisoformat("2024-01-01 00:00:00").timestamp())

# Generate JSON files with random fields.
#
# Every record is guaranteed to have two fields:
# - id          int
# - timestamp   ISO format timestamp
#
# Records can have the following fields:
# - col1        float, range [100, 200)
# - col2        float, range [200, 300)
# - col3        float, range [300, 400)
# - tags        List[str], possible values "a", "b", "c", "d"
#
# Saved as data/{{ id }}_record.json
for id in range(1, 26):
    record = {"id":id,
              "timestamp":datetime.fromtimestamp(random.randrange(start_timestamp, end_timestamp)).isoformat(),
              }
    fields = random.sample(optional_fields, random.randint(0, len(optional_fields)))
    for field in fields:
        record[field] = 100*(random.random() + int(field[-1]))
    tags = random.sample(optional_tags, random.randint(0, len(optional_tags)))
    if tags:
        record["tags"] = tags
    with open(f"data/{id}_record.json", "w") as f:
        json.dump(record, f)

# Generate DataFrames with random fields.
#
# Each DataFrame has 20 rows.
# Every row is guaranteed to have two fields:
# - id          int
# - timestamp   ISO format timestamp
#
# Rows can have the following fields:
# - col1        float, range [100, 200)
# - col2        float, range [200, 300)
# - col3        float, range [300, 400)
# - tags        List[str], possible values "a", "b", "c", "d"
#
# Each DataFrame is saved as data/df_{{ df_id }}.parquet
for df_id in range(1, 6):
    df = pd.DataFrame()
    for id in range(1, 21):
        record = {"id":100*df_id+id,
                "timestamp":datetime.fromtimestamp(random.randrange(start_timestamp, end_timestamp)).isoformat(),
                }
        fields = random.sample(optional_fields, random.randint(0, len(optional_fields)))
        for field in fields:
            record[field] = 100*(random.random() + int(field[-1]))
        tags = random.sample(optional_tags, random.randint(0, len(optional_tags)))
        if tags:
            record["tags"] = tags
        
        df_temp = pd.DataFrame([record])
        df = pd.concat([df, df_temp])
    df.to_parquet(f"data/df_{df_id}.parquet", index=False)
