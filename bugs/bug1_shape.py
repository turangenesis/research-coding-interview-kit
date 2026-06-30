# BUG 1 — SHAPE MISMATCH (the #1 ML bug).
# Run it:  python bugs/bug1_shape.py
# It will crash. Read the error, then fix it (or ask: et-debug).
import torch
import torch.nn as nn

layer = nn.Linear(10, 2)      # expects inputs with 10 features
x = torch.randn(8, 16)        # but this has 16 features (batch=8)
out = layer(x)                # RuntimeError: mat1 and mat2 shapes cannot be multiplied
print(out.shape)

# HINT to practice the habit: print(x.shape) and check what the layer expects.
