# 🃏 Cheat Card — keep this open during the call

## Setup
When they ask "is your environment ready?" → **"Yes."**
```
mkdir NAME && cd NAME                                  # clean folder
python3 -m venv .venv && source .venv/bin/activate     # env ON  (prompt shows (.venv))
pip install -r requirements.txt                        # if they give a repo with one
pip install torch==2.6.0 transformers==4.50.3 datasets==3.5.0   # else, exact pins
python FILE.py                                          # run a script
git clone URL && cd REPO                               # if they give a repo
```

## How the AI sees your error (pick fastest)
- In an IDE extension: type **`@terminal`** → it reads your terminal output (no paste).
- Or it reads the **Problems panel** (red squiggles) automatically.
- Or **paste** the error. Or **let the assistant run the command itself** — then it has code AND output.

---

# HOW TO THINK (this is what they score)

## THE ONE RULE
Every bug is **LOUD** (it crashes — the traceback's LAST line names the family) or **SILENT** (it runs and prints a WRONG number — only YOUR judgment catches it).
After EVERY run say: **"print the shape — and is this value even plausible?"**
**You are the senior; the AI is the intern.**

## THE LOOP (say each step out loud)
1. REPRODUCE — "First I just run it and see." (don't theorize first)
2. READ — loud: last line. silent: shape AND value.
3. CATEGORIZE — "shape / dtype / device / config / dim / semantic?"
4. HYPOTHESIZE — "I think X because Y." (BEFORE touching the AI)
5. FIX — AI as fast intern: "confirm my hypothesis / apply that fix."
6. VERIFY — re-run. Never declare done without re-running.

## 🔴 LOUD families (it crashes; read the last line)
- **SHAPE** "shapes cannot be multiplied" → print `.shape` of each side.
- **DTYPE** "expected Long but got Float" → token ids must be `.long()`.
- **DEVICE** cuda error → `device = "cuda" if torch.cuda.is_available() else "cpu"` (Mac: "mps").
- **CONFIG** KeyError / checkpoint mismatch / input too long → check what exists / the real limit.

## 🟡 SILENT families (it runs; the number lies — high signal)
- **DIM** argmax/sum/mean missing/wrong `dim` → output shape wrong → `argmax(dim=-1)`.
- **SEMANTIC** absurd value (0%/100% acc, loss frozen/exploding) → comparing preds vs labels? called `zero_grad()`? used `no_grad()`/`eval()`?

## SANITY SNIPPETS (to INVESTIGATE, not fix)
```
print(x.shape, x.dtype, x.device)    # every tensor answers these 3
print(ds.column_names)               # before indexing a dataset
print(preds, labels)                 # before trusting any accuracy
```

## If you freeze
"Let me reproduce it first and just look at the output before I theorize."
Buys time AND shows method. Calm + verifying > fast + wrong.

## Meta (for any new domain)
Thrashing on details? **Ask for the MAP first, details second.**
