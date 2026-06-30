# BUG 10 — long input crashes the model: text exceeds the max sequence length.
# Run it:  python bugs/bug10_truncation.py
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

ckpt = "distilbert-base-uncased-finetuned-sst-2-english"
tok = AutoTokenizer.from_pretrained(ckpt)
model = AutoModelForSequenceClassification.from_pretrained(ckpt)

long_text = "good " * 1000               # ~1000 tokens, model max is 512
enc = tok(long_text, return_tensors="pt") # BUG: no truncation -> sequence too long
with torch.no_grad():
    out = model(**enc)                    # error: index/size out of range (position embeddings)
print(out.logits)

# HINT: models have a max length; longer inputs must be cut.
# FIX: tok(long_text, truncation=True, max_length=512, return_tensors="pt")
