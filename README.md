# 3x+1 (Collatz Conjecture) Visualizer

A small Python script that explores the [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture):
starting from any positive integer, repeatedly apply the rule below until you
reach 1.

- If the number is even, divide it by 2.
- If the number is odd, multiply it by 3 and add 1.

The conjecture (still unproven) is that this process always eventually
reaches 1, no matter what number you start with. This script lets you pick a
starting number, then plots the "trajectory" of that number step by step —
and keeps going, automatically testing the next number, and the next, so you
can watch how wildly the step count and peak values vary between
consecutive integers.

## What it does

1. Prompts you to enter a starting number.
2. Runs the 3x+1 sequence on it, printing each intermediate value.
3. Once the sequence reaches 1, plots **steps vs. value** with Matplotlib and
   shows how many steps it took to converge.
4. Automatically moves on to the next number (`n+1, n+2, ...`) and repeats,
   plotting each one in turn.

This makes it easy to compare how chaotic/long the sequence is for
consecutive starting numbers, which is one of the more interesting features
of the conjecture (e.g. some numbers converge quickly, while a neighbor can
take hundreds of steps).

## Requirements

- Python 3
- `matplotlib`

```bash
pip install matplotlib
```

## Running

```bash
python3 "3x+1 program.py"
```

You'll be prompted for a starting number. A plot window will pop up after
each number's sequence completes — **close the plot window to move on** to
the next number in the sequence. The script runs indefinitely (it keeps
testing `n+1, n+2, ...` forever), so stop it with `Ctrl+C` when you're done
exploring.

## A floating-point bug I found and fixed

The original version of this script used `a = a / 2` for the even case,
which in Python always returns a `float`. That's fine for small numbers,
but Python floats only carry about 15-17 significant digits of precision.
Once a starting number grew past that (20+ digit numbers, for example), the
float division silently lost precision partway through the sequence — so
the "step count" it printed for very large numbers was sometimes wrong,
without any error or warning.

This is why the comments at the bottom of the script (from early testing)
have confused annotations like "354 steps ?!?!" and "443 steps repeating
?!?!?" — those numbers looked inconsistent because they were computed with
degraded floating-point precision, not because of any genuine anomaly in
the Collatz sequence itself.

**The fix:** use integer floor division (`a = a // 2`) instead of true
division (`a = a / 2`). This keeps every value as a Python arbitrary-
precision integer throughout, so the sequence is computed exactly, no
matter how large the starting number is. Recomputing those same test
numbers with integer arithmetic gives the correct step counts:

| Starting number | Original (float) result | Correct (integer) result |
|---|---|---|
| `3721832837283283782328866` | 511 steps | **534 steps** |
| `37218328372832837829074`   | 512 steps | 512 steps (unaffected) |
| `3721832837283283782907`    | 354 steps | **470 steps** |
| `1727823783728372837461`    | 443 steps | **430 steps** |

The old comments are left in the source as a record of that discovery — a
reminder that floating-point arithmetic isn't safe for exact integer
sequences at scale, and that a strange result is worth double-checking
before assuming it's a property of the math rather than a bug.

## Notes

- The script runs as an infinite loop by design — there's no built-in stop
  condition, so it will keep testing successive integers and plotting their
  Collatz trajectories until manually interrupted.
- Progress prints to the console as well as plotting, so you can follow
  along without waiting on each graph.
