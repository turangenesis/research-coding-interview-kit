# BUG 7 — using a column name the dataset doesn't have (a real data bug).
# Run it:  python bugs/bug7_columns.py
from datasets import load_dataset

ds = load_dataset("glue", "sst2", split="validation[:5]")
for row in ds:
    print(row["text"])     # BUG: sst2's text column is "sentence", not "text" -> KeyError

# HINT: when a column is missing, look at what actually exists.
# FIX: print(ds.column_names) first, then use row["sentence"].
