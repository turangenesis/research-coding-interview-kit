# BUG 4 — CAN'T BATCH VARIABLE-LENGTH SEQUENCES (a classic dataloader/collate bug).
# Run it:  python bugs/bug4_padding.py
# Sentences have different lengths, so they can't stack into one tensor. Fix it.
import torch
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("distilbert-base-uncased")
texts = ["short", "a much longer sentence right here please"]

ids = [tok(t)["input_ids"] for t in texts]   # BUG: ragged lists, different lengths
batch = torch.tensor(ids)                     # ValueError: expected sequence of length N
print(batch.shape)

# HINT: the tokenizer can pad for you ->  tok(texts, padding=True, return_tensors="pt")
