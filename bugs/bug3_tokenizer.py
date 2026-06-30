# BUG 3 — TOKENIZER / MODEL MISMATCH (different checkpoints).
# Run it:  python bugs/bug3_tokenizer.py
# The tokenizer is BERT (returns token_type_ids); the model is DistilBERT
# (doesn't accept them). Read the error, then fix it.
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tok = AutoTokenizer.from_pretrained("bert-base-uncased")                                   # BUG: wrong family
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

enc = tok("I loved this movie", return_tensors="pt")
with torch.no_grad():
    out = model(**enc)            # TypeError: unexpected keyword argument 'token_type_ids'
print(out.logits)

# HINT: tokenizer AND model must come from the SAME checkpoint.
