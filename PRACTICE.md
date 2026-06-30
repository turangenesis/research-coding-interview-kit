# Practice Plan — do the reps, don't just read

You're not preparing to be a framework expert. You're preparing to **run things, read errors calmly, fix small, and narrate clearly while pairing with an AI assistant.** That's the whole test. This kit gets you there in a few focused hours.

## Step 0 — environment (15 min, once)
```bash
bash setup.sh
source .venv/bin/activate
# optional, if a task needs gated models:  huggingface-cli login
```
Read `setup.sh` — it's just: make a `.venv`, install the pins, verify imports. Nothing magic. Use it for a clean workspace; never run it inside someone else's configured project.

## Step 1 — RUN A MODEL (15 min) ← do this first; it removes the fear
```bash
python 01_hello_hf.py
```
Watch `text → tokenize → model → logits → argmax → label` happen. **You've now run a model.** Read the file; understand each step.

## Step 2 — debug the 10 bugs WITH your assistant (2–3 hrs) ← the core rep
For each file in `bugs/`:
1. Run it → see it fail (or print a wrong number).
2. **Read the error out loud**, last line first. Form a hypothesis.
3. Ask your AI assistant: *"this fails with X — root cause + smallest fix?"* Let it propose; **you run it to verify.**
4. Check yourself against `bugs/FIXES.md`.
5. Say the one-line explanation out loud.

Then do them **again without the assistant**, to feel the families: **shape · dtype · device · tokenizer · padding · dim · metric · training · columns · truncation.**

## Step 3 — build tiny things from scratch (2–4 hrs)
Have the assistant scaffold; you run + verify each:
- Load a dataset → print columns, labels, a few rows.
- Tokenize a batch (padding/truncation) → print `input_ids.shape`.
- Run inference → compute accuracy **by hand**: `(preds == labels).float().mean()`.
- Add one thing: a log line, a batch loop, or precision/recall.

This mirrors the 10 task types in `TASK_TYPES.md`.

## Step 4 — mock the pairing (1 hr)
Screen-share to yourself. Take any bug/task and **narrate the whole way**:
> "First I reproduce. … reading the traceback bottom-up. … looks like a shape issue, let me print the shapes. … I'll ask the assistant for a fix and then run it to verify."

## The 4 things they actually grade
1. **Environment** — can you get the stack running? (Step 0)
2. **Debugging** — read an error, inspect shapes/tokenization/outputs. (Step 2)
3. **Research coding** — move slowly, test small, use the assistant well. (Step 3)
4. **Communication** — narrate what you're checking and why. (Step 4)

Calm > clever. Run small. Say what you see. You've got this.
