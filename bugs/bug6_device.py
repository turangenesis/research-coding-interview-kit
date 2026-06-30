# BUG 6 — code hardcodes a GPU ("cuda") on a machine that doesn't have one (VERY common).
# Run it:  python bugs/bug6_device.py
import torch
import torch.nn as nn

device = "cuda"                       # BUG: assumes a GPU exists
model = nn.Linear(4, 2).to(device)    # crashes on a CPU/Mac machine
x = torch.randn(3, 4).to(device)
print(model(x).shape)

# HINT: never hardcode the device. Detect it.
# FIX: device = "cuda" if torch.cuda.is_available() else "cpu"   (on Mac you can also use "mps")
