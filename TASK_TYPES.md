# 10 Task Types & How to Reason Out Loud

For each: what they might ask · how to attack it · what to **SAY** (the reasoning is half the score). You don't memorize code — you narrate a calm loop. Every task below is a variation of: **run small → read → hypothesize → ask the AI → verify → explain.**

### 1. Load a dataset
**Do:** `ds = load_dataset(name, split="...[:20]")` → print `ds.column_names`, `ds[0]`.
**Say:** "I'll load a small slice and inspect columns, labels, and a couple rows before doing anything."

### 2. Tokenize text
**Do:** `AutoTokenizer.from_pretrained(ckpt)`; `tok(texts, padding=True, truncation=True, return_tensors="pt")`; print `input_ids.shape`.
**Say:** "Pad and truncate so the batch is even; check input_ids is (batch, seq_len)."

### 3. Run model inference
**Do:** `with torch.no_grad(): logits = model(**enc).logits`; `preds = logits.argmax(dim=-1)`; map with `id2label`.
**Say:** "no_grad because it's inference; logits are (batch, classes); argmax over the class dim is the prediction."

### 4. Debug a broken script (most likely)
**Do:** run → read bottom-up → name the family (shape/dtype/tokenizer/padding/device/logic) → smallest fix → re-run.
**Say:** "Let me reproduce first. The last line points to a [shape] problem; I'll print the shapes to confirm, then make the smallest fix."

### 5. Create a tiny classifier
**Do:** dataset → tokenizer → model → a minimal loop (or `Trainer`).
**Say:** "I'll wire the smallest end-to-end path, then confirm the loss moves before scaling."

### 6. Evaluate results
**Do:** `acc = (preds == labels).float().mean()`; mention precision/recall, false pos/neg.
**Say:** "Accuracy is preds vs labels — but I'd also look at error types; false positives vs negatives matter differently."

### 7. Compare two model outputs
**Do:** state a criterion, compare on it, name failure modes.
**Say:** "To compare fairly I need a metric. On [criterion] A is better, but I'd watch for [failure mode] and test on harder examples."

### 8. Modify research code
**Do:** one small, verified change (logging / metric / batching / filter).
**Say:** "I'll make the smallest change that adds [X], run it to confirm nothing else moved, then explain it."

### 9. Use the AI assistant well (always being watched)
**Do:** ask for scaffolding, READ its output, run to verify, say why you accept/reject.
**Say:** "I'll let it scaffold, but I'm reading before I run — I accept this part because X, I'd change this because Y."

### 10. Research reasoning
**Do:** state a hypothesis, a way to test it, the threats to validity.
**Say:** "My hypothesis is X. I'd test it with [small experiment]. It'd be unreliable if [leakage / too few samples / overfitting], so I'd check that."

---
**The mindset:** they grade **calm + reasoning + AI-assisted debugging + clear talk** — not framework trivia. Reproduce, narrate a hypothesis, use the assistant, verify by running. That's a pass.
