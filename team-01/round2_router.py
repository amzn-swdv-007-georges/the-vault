# ============================================================
# ROUND 2 - ROUTER (DO NOT EDIT)
# Run:   python round2_router.py
# Tests round2_rules.py with several names and shows
# the current state of the system.
# ============================================================

import os

RULES_FILE = os.path.join(os.path.dirname(__file__), "round2_rules.py")

test_callers = [
    "Alice",
    "Bob",
    "VegemiteFan",
    "SpamBot",
    "TrollGuy",
    "Charlie",
    "Diana",
    "vegemitefan",
]


def load_rules_with_caller(path, caller):
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()
    new_lines = []
    replaced = False
    for line in original.splitlines():
        stripped = line.lstrip()
        if (not replaced) and stripped.startswith("caller_name") and "=" in stripped:
            new_lines.append(f'caller_name = {caller!r}')
            replaced = True
        else:
            new_lines.append(line)
    if not replaced:
        new_lines.insert(0, f'caller_name = {caller!r}')
    return "\n".join(new_lines)


print("=== Round 2 - System Check ===")
print()

on_air_count = 0
blocked_count = 0

for name in test_callers:
    code = load_rules_with_caller(RULES_FILE, name)
    local_env = {}
    try:
        exec(code, local_env)
    except Exception as e:
        print(f"  Caller: {name:<14} -> ERROR in round2_rules.py: {e}")
        continue

    on_air = bool(local_env.get("on_air", False))
    status = "ON AIR" if on_air else "blocked"
    print(f"  Caller: {name:<14} -> {status}")

    if on_air:
        on_air_count += 1
    else:
        blocked_count += 1

print()
print("--- System state ---")
print(f"Total on air:   {on_air_count}")
print(f"Total blocked:  {blocked_count}")
