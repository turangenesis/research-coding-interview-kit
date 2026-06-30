# Research-Coding Interview Kit

**A runnable kit + the mental map for AI-assisted / ML coding-pairing interviews.** Run a model, debug the 10 classic bugs, and learn the *one loop* that handles almost any task they throw at you — calmly, while pairing with an AI assistant.

> The modern ML/research interview isn't LeetCode. It's: *"here's a real problem and an AI assistant — pair with us, debug calmly, reason out loud."* This kit trains exactly that.

---

## Why this exists (the hidden curriculum)

There's a skeleton that every working engineer uses **automatically** — open a folder, set up an environment, get the task, run a debugging loop. It's *common to do* but **almost never written down**, because the people who know it forget they know something teachable. So newcomers spend hours (or weeks) reconstructing it from fragments under pressure.

This repo makes that skeleton **explicit and runnable.** Read [`THE_MAP.md`](THE_MAP.md) once, do the reps, and you'll walk into a pairing interview with a method instead of a fog.

## The 30-second map

```
SETUP         folder → environment → "ready" → task (file / repo / blank)
THE LOOP      reproduce → read → categorize → hypothesize → fix → VERIFY (re-run)
THE RULE      every bug is LOUD (it crashes) or SILENT (it prints a wrong number).
              after every run, ask: "print the shape — and is this value even plausible?"
FAMILIES      10 bugs → 6 families. LOUD: shape · dtype · device · config
                                    SILENT: dim · semantic
              name the family, say its one-liner, fix, re-run. (full table in THE_MAP.md)
MINDSET       you are the senior; the AI is the intern. calm > clever. narrate everything.
META          stuck / thrashing on details? ask for the MAP first, details second.
```

## Quickstart

```bash
git clone https://github.com/turangenesis/research-coding-interview-kit
cd research-coding-interview-kit
bash setup.sh                 # venv + the pinned deps (edit requirements.txt to match your interview)
source .venv/bin/activate
python 01_hello_hf.py         # ← run a real model end-to-end. removes the fear.
python bugs/bug1_shape.py     # ← then debug the 10 classic bugs, one rep at a time
```

## What's inside

| File | What it does |
|---|---|
| [`THE_MAP.md`](THE_MAP.md) | the universal skeleton: setup + the debug loop + the meta-skill |
| [`SETUP_FAQ.md`](SETUP_FAQ.md) | the chat vs terminal vs venv confusion, answered — who runs what, and what `git clone` really does |
| [`CHEATCARD.md`](CHEATCARD.md) | one-page reference to keep open during the call |
| `setup.sh` | one command: isolated env + pinned deps + verified imports |
| `01_hello_hf.py` | the whole HF flow, working: text → tokenize → model → logits → label |
| `bugs/bug1..10.py` | the **10 classic ML bugs** — shape · dtype · device · tokenizer · padding · dim · metric · training · columns · truncation |
| [`bugs/FIXES.md`](bugs/FIXES.md) | solutions + the one sentence to *say* for each |
| [`PRACTICE.md`](PRACTICE.md) | a focused practice plan (do the reps, don't just read) |
| [`TASK_TYPES.md`](TASK_TYPES.md) | 10 likely task types + how to reason out loud on each |

## The philosophy

- **You are the senior; the AI is the intern.** Let it scaffold and propose — but you reproduce, hypothesize, and **verify by running.** That verifying is the skill they grade.
- **Every bug is LOUD or SILENT — and collapses into one of 6 families.** Loud crashes (read the last traceback line): *shape · dtype · device · config*. Silent ones print a wrong number — only your judgment catches them: *dim · semantic*. After every run: *"print the shape — and is this value plausible?"* Naming the family is what tells you the one sentence to say next.
- **Calm > clever.** Reproduce first, narrate your method, run the smallest test, never declare victory without re-running.
- **Ask for the map first.** When you're new to anything and thrashing on details, the move isn't "ask fewer questions" — it's *"ask the framing question first, details second."*

## Who it's for

Anyone facing an **AI-assisted / ML / research-coding pairing interview** (Hugging Face, PyTorch, transformers, datasets) who wants to walk in calm and methodical instead of panicked. The *thinking* (the loop + the meta-skill) is language-agnostic; the *practice* is ML-flavored.

## License

MIT — use it, fork it, share it. If it helps you, ⭐ it so others find it.

---

Built by **Emre Turan** · [turangenesis.com](https://turangenesis.com)
