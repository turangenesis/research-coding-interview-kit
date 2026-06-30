# SETUP FAQ — the chat, the terminal, and the venv (who runs what)

`THE_MAP.md` shows setup when **you** drive a terminal. But in an AI-assisted interview you're often typing into a **chat panel** while a **terminal sits below it** — and that raises a set of questions almost nobody writes down. If you've ever thought *"wait, is the venv even on in this chat?"* — this page is for you.

The whole confusion dissolves once you hold one fact:

> **The chat and the terminal are TWO SEPARATE shells.** The AI assistant runs commands in *its own* hidden shell — not the terminal panel you see.

---

## Q1 — Is the venv "activated in this chat"?

Wrong frame — and that's the unlock. **A venv is a property of a *terminal*, not of a chat.** The chat has no venv state to be on or off.

- Your **bottom terminal** shows `(.venv)` → *that terminal* has it active. ✅
- The **chat / assistant** has its own separate shell and switches the venv on **inside each command it runs**.

So "is the venv on in the chat?" has no answer — it's like asking what color the number 7 is.

## Q2 — Do I need a terminal open, with venv activated, for the assistant to work?

**No.** The assistant has its own shell and activates the venv itself, per command. You do **not** need the bottom terminal open at all. (It's there for when *you* want to run something by hand.)

## Q3 — Do I need to tell the assistant "activate the venv and run xyz"?

**No.** It already knows the folder and its `.venv`, and turns it on automatically when it needs Python. Just ask in plain English: *"run this file,"* *"load this dataset,"* *"debug this error."* No special command words, no `/orient` / `/onboard` rituals required.

## Q4 — Then why was I told to run `cd ~/path && source .venv/bin/activate` *before* launching the assistant?

Two reasons — only the first matters:

- **`cd ~/path`** ← **this part matters.** It launches the assistant pointed at the right folder.
- **`source .venv/bin/activate`** ← only for **YOU**, so *your own* `python`/`pip` commands in the bottom terminal use the right environment. Not required for the assistant.

## Q5 — Does activating / deactivating the venv over and over hurt anything?

**Completely harmless.** Activating just sets a few invisible "use this Python" pointers — it installs nothing, downloads nothing, modifies no files. Do it a thousand times; the venv is unchanged.

> Mental model: `.venv` is a **toolbox sitting in the folder.** "Activating" = picking it up. You can pick it up and set it down endlessly; the tools inside never change.

## Q6 — So what actually makes any of this possible?

> **The only thing that ever mattered is that the `.venv` lives in the folder.**

Activation is just *pointing a shell at it*. The assistant can point at it anytime; you can point at it in your terminal anytime. The environment itself is the folder. Get that and the rest is noise.

---

## Q7 — `git clone URL` — what does it actually do? (the simplest version)

**"Download a copy of an online code project into a new subfolder inside where I am."** That's the whole thing.

| Your worry | Reality |
|---|---|
| "Takes me out of my folder?" | **No.** You stay put; it creates a **subfolder** inside the current one. |
| "Deactivates the venv?" | **No.** The venv survives even when you `cd` into the new subfolder — only the directory changes, the Python stays. |
| "Creates its own separate workspace?" | **No.** It only writes **files** to disk. No new window, no new environment. |

Before:
```
interview/  →  .venv, requirements.txt
```
After `git clone <url>` (repo called "YZ"):
```
interview/  →  .venv, requirements.txt, YZ/   ← new folder of downloaded code
```
Then `cd YZ` to work inside it. Venv still active.

⚠️ One real gotcha: if the cloned repo has **its own `requirements.txt`**, installing it goes into your *current* active venv and may change your torch/transformers versions. Usually fine — just narrate it: *"this repo wants different versions, installing them into the venv."*

---

## The one sentence to remember

**You talk to the assistant in plain English; it handles the venv and the commands itself — the only thing that ever mattered is that the `.venv` lives in the folder.**

## 60-second sanity check before the call
1. Open Terminal → `cd` into your interview folder → launch the assistant (`claude`, or open the folder in Cursor).
2. Ask it: *"run a one-line smoke test that imports torch, transformers, datasets and prints the versions."*
3. See versions print → you're live. If not, the error names the missing piece — hand it to the assistant and narrate.
