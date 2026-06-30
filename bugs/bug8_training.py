# BUG 8 — training loop that won't learn properly: gradients never reset.
# Run it:  python bugs/bug8_training.py  (it runs, but the loss behaves badly)
import torch
import torch.nn as nn

model = nn.Linear(4, 1)
opt = torch.optim.SGD(model.parameters(), lr=0.1)
x = torch.randn(16, 4)
y = torch.randn(16, 1)

for step in range(5):
    pred = model(x)
    loss = ((pred - y) ** 2).mean()
    loss.backward()
    opt.step()
    # BUG: never called opt.zero_grad() -> gradients ACCUMULATE across steps
    print("step", step, "loss", round(loss.item(), 4))

# HINT: in PyTorch, gradients add up unless you clear them each step.
# FIX: call opt.zero_grad() at the start of the loop (before backward).
