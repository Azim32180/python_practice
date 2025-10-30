## Setup

Create a virtual environment and install dependencies:

```bash
# Create virtual environment
python3 -m venv testenv

# Activate virtual environment
source testenv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Run

Example command and output:

```bash
python3 make_emoji.py --name :sparkles: --msg "Hello"
```

**Output:**

```
✨ Hello
```

Additional examples:

```bash
# Default rocket emoji
python3 make_emoji.py

# Custom emoji with message
python3 make_emoji.py --name :fire: --msg "Great job!"
```

## Time

Run:

```bash
python3 -m timeit -n 1000 -s "from emoji import emojize" "emojize(':rocket:')"
```

**Result:**

```
1000 loops, best of 5: 3.54 nsec per loop
```

## Run tests using pytest:

```bash
pytest -q
```

Expected output:

```
.                                                                     [100%]
1 passed in 0.12s
```

![alt text](<Screenshot 2025-10-30 at 5.54.18 PM.png>)
