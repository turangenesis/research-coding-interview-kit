# BUG 2 — WRONG TENSOR DTYPE.
# Run it:  python bugs/bug2_dtype.py
# Token IDs must be integers (long), not floats. Read the error, then fix it.
import torch
import torch.nn as nn

embedding = nn.Embedding(100, 8)          # vocab of 100, dim 8
token_ids = torch.tensor([1.0, 2.0, 3.0]) # BUG: these are floats
out = embedding(token_ids)                # error: expected Long/Int, got Float
print(out.shape)

# HINT: token ids are indices -> they must be .long().
