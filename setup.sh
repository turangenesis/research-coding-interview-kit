#!/usr/bin/env bash
# ── One-command environment setup ──
# Not magic — it just runs the commands you'd type by hand, bundled so you
# don't fumble live. Read it; every line is plain.
#
# USE IT: to set up a CLEAN practice/interview workspace.
# DON'T use it: inside a project that already has its own env/requirements — use theirs.
set -e

echo "→ 1. creating an isolated Python environment (.venv)..."
python3 -m venv .venv
source .venv/bin/activate

echo "→ 2. installing the pinned versions (edit requirements.txt to match YOUR interview)..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

echo "→ 3. verifying the imports work..."
python -c "import torch, datasets, transformers; print('OK — torch', torch.__version__, '| transformers', transformers.__version__, '| datasets', datasets.__version__)"

echo ""
echo "Environment ready. Reactivate later with:  source .venv/bin/activate"
echo "Next:  python 01_hello_hf.py"
