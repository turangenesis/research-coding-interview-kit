"""
01 — THE WHOLE HUGGING FACE FLOW, working end to end.
Run it:  python 01_hello_hf.py

This is the thing you said you've never done: load a model, run it, see output.
After this runs once, you have RUN A MODEL. The flow below is 90% of the interview:
    text  ->  tokenize  ->  model  ->  logits  ->  argmax  ->  label
"""
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# A small, public sentiment model. First run downloads ~270MB (one time).
ckpt = "distilbert-base-uncased-finetuned-sst-2-english"
print("loading tokenizer + model (first run downloads ~270MB)...")
tok = AutoTokenizer.from_pretrained(ckpt)
model = AutoModelForSequenceClassification.from_pretrained(ckpt)
model.eval()

texts = [
    "I absolutely loved this movie.",
    "This was a complete waste of time.",
    "It was fine, nothing special.",
]

# 1. TOKENIZE — turn text into model inputs. padding=True so they batch evenly.
enc = tok(texts, padding=True, truncation=True, return_tensors="pt")
print("tokenized input_ids shape:", enc["input_ids"].shape)  # (batch, seq_len)

# 2. RUN THE MODEL — no_grad = inference, no training.
with torch.no_grad():
    logits = model(**enc).logits
print("logits shape:", logits.shape)  # (batch, num_classes)

# 3. INTERPRET — argmax over the class dimension, map to a label.
preds = logits.argmax(dim=-1)
id2label = model.config.id2label
print()
for text, p in zip(texts, preds):
    print(f"  {id2label[p.item()]:9s} <-  {text}")

print("\n✅ You just ran a model. That flow (tokenize -> model -> argmax -> label) is the spine of almost everything they'll ask.")
