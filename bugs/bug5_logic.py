# BUG 5 — NO CRASH, BUT THE ANSWER IS WRONG (a silent logic bug — the hardest kind).
# Run it:  python bugs/bug5_logic.py
# It prints an accuracy, but the number is nonsense. WHY? (This tests reasoning, not error-reading.)
import torch

logits = torch.tensor([[2.0, 1.0],   # row 0 -> class 0
                       [0.5, 3.0],   # row 1 -> class 1
                       [1.0, 0.2]])  # row 2 -> class 0
labels = torch.tensor([0, 1, 0])     # the correct answers

preds = logits.argmax()              # BUG: no dim! argmax over the FLATTENED tensor -> one number
acc = (preds == labels).float().mean()
print("predictions:", preds)
print("accuracy:", acc.item())

# HINT: you want the best class PER ROW -> argmax(dim=-1). Print preds to SEE the bug.
