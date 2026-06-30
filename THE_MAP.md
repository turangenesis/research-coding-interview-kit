# THE MAP — setup, debugging, and the meta-skill

The skeleton it takes most people hours (or months) to assemble — here top-down, in one page. Reusable for any coding-pairing interview and any new project.

## Part 0 — the meta-skill (saves you the hours next time)

When you feel the signal — *"every answer reveals a new nuance," "I keep getting the mental model wrong," "I'm thrashing on details"* — **STOP and zoom out. Ask for the MAP, not the tile:**

- "Give me the entire flow end-to-end, simplest version, before any details."
- "What's the mental model / the 5 steps — and which am I on?"
- "Show me the simplest complete example, start to finish."

**Lead with the map; details then land inside a structure instead of fog.** This is universal to learning anything new.

## Part 1 — SETUP (any local coding task)

Make a clean folder, turn on an isolated Python environment with the right versions:

```bash
mkdir interview && cd interview
python3 -m venv .venv && source .venv/bin/activate     # prompt now shows (.venv)
pip install -r requirements.txt    # if they gave one
# else install exactly what's specified, e.g.:
pip install torch==2.6.0 transformers==4.50.3 datasets==3.5.0
```

**Two independent things — don't conflate them:**
- The folder you start your AI assistant in = **where it works**.
- The active venv = **which packages exist**.
They never conflict. (Pro tip: a ready venv can be activated from *any* folder by absolute path — `source ~/path/.venv/bin/activate` — only the Python switches; your folder stays.)

**When they ask "is your environment ready?" → "Yes."** Then the task arrives — one of three:

| They give… | You do |
|---|---|
| A **file** | drag/save it into the folder → `python file.py` |
| A **repo link** | `git clone URL && cd REPO` → (if present) `pip install -r requirements.txt` |
| **"Build X"** (blank) | just start — AI scaffolds, you run + verify |

## Part 2 — THE DEBUG LOOP (any bug, any language)

**The one rule:** every bug is **LOUD** (it crashes — the traceback's last line names the family) or **SILENT** (it runs and prints a *wrong value* — only your judgment catches it). After every run: *"print the shape — and is this value even plausible?"*

**The loop — say each step OUT LOUD:**
1. **REPRODUCE** — "First I just run it and see what happens." (don't theorize first)
2. **READ** — loud bug: read the last line. silent bug: look at shape AND value.
3. **CATEGORIZE** — "Is this shape / dtype / device / config / dim / semantic?"
4. **HYPOTHESIZE** — "I think X because Y." (say it *before* touching the AI)
5. **FIX** — AI as a fast intern: "confirm my hypothesis / apply that fix."
6. **VERIFY** — re-run. "Now it makes sense because Z." Never declare done without re-running.

**You are the senior; the AI is the intern.** They grade the loop and your narration, not trivia.

### The bug families (what to say)
| Family | Signature | Say |
|---|---|---|
| 🔴 Shape | "shapes cannot be multiplied" | "print `.shape` of each side, find the wrong dim" |
| 🔴 Dtype | "expected Long but got Float" | "token ids are indices — must be `.long()`" |
| 🔴 Device | "tensors on different devices" | "never hardcode cuda — detect it" |
| 🔴 Config | KeyError, checkpoint/length mismatch | "check what exists / the real limit before guessing" |
| 🟡 Dim | output shape wrong (scalar vs vector) | "needs `argmax(dim=-1)` — it collapsed" |
| 🟡 Semantic | the *value* is absurd (0%/100% acc) | "am I comparing preds to labels, not logits?" |

## Part 3 — is this "the universal map"? (honest scope)

- **The debug loop** (reproduce → read → categorize → hypothesize → fix → verify) → **universal.** Any language, any project. Never changes.
- **The setup shape** (folder → environment → task → loop) → **universal.** Only the tools differ: Python uses `venv`/`pip`; JS uses `npm`; same skeleton, swap commands.
- **The meta-skill** (ask for the map first) → **universal** to learning anything new.

You now own the skeleton — that's the part that transfers to every future project.
