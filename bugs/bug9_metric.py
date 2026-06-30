# BUG 9 — accuracy is wrong: comparing raw logits to labels instead of predictions.
# Run it:  python bugs/bug9_metric.py  (no crash, just a nonsense number)
import torch

logits = torch.tensor([[2.0, 1.0],
                       [0.5, 3.0],
                       [1.0, 0.2],
                       [0.1, 0.9]])
labels = torch.tensor([0, 1, 0, 1])

# BUG: comparing the (4,2) logits to the (4,) labels, not the predicted classes
acc = (logits == labels).float().mean()
print("accuracy:", acc.item())

# HINT: accuracy compares PREDICTIONS to labels, and a prediction is the best class per row.
# FIX: preds = logits.argmax(dim=-1); acc = (preds == labels).float().mean()
