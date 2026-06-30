# FIXES — try each bug yourself FIRST, then check here

The goal isn't the fix — it's the **habit**: run → read error → isolate the layer → fix → re-run → explain.

### Bug 1 — shape mismatch
`x` has 16 features but the layer expects 10. Either `nn.Linear(16, 2)` or make `x = torch.randn(8, 10)`.
**Say:** "Shape error — the layer's in_features doesn't match the input's last dim. I'll print both and align them."

### Bug 2 — dtype
Embedding indices must be integers: `token_ids = torch.tensor([1, 2, 3])` or `.long()`.
**Say:** "Token ids are indices, so they must be long, not float."

### Bug 3 — tokenizer/model mismatch
Load both from the same checkpoint: `tok = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")`. (Or drop `token_type_ids` before calling the model.)
**Say:** "The tokenizer and model came from different families — they must match."

### Bug 4 — padding
Let the tokenizer pad + return tensors: `enc = tok(texts, padding=True, return_tensors="pt")`, then use `enc["input_ids"]`.
**Say:** "Variable-length sequences can't stack — I'll pad them to the same length."

### Bug 5 — logic (the important one)
`argmax` needs the class dimension: `preds = logits.argmax(dim=-1)`. Without `dim`, it flattens everything into one number.
**Say:** "No crash, but `preds` isn't one-per-row — argmax flattened it. I want argmax over the class dim."

---
**The pattern in all five:** you didn't need to be a PyTorch expert. You ran it, read the signal, named the layer (shape / dtype / tokenizer / batching / logic), made the smallest fix, re-ran. **That is the whole interview.**
