# Alien Vault

> Progressive Python encapsulation activities using classes, objects, protected attributes, private attributes, controlled methods, and properties.

## Repository Workflow

- One student is the engineer for each activity.
- The engineer shares their screen.
- All file changes are typed manually.
- Do not use Open Code.
- The engineer completes the full activity.
- The engineer runs and tests the required script.
- The engineer commits and pushes the changes.
- The engineer tags the next student.
- Everyone else pulls, reviews, and tests the latest version.

## Initial Setup

Authenticate Codio with GitHub:

```bash
gh auth login
```

Clone the repository:

```bash
git clone <repository-url>
cd alien-vault
```

Before starting an activity, pull the latest version:

```bash
git pull
```

After completing an activity:

```bash
git add .
git commit -m "Complete Activity X"
git push
```

Replace `X` with the activity number.

---

## Activities Architecture

```text
alien-vault/
├── Activity 1 — The Empty Vault
│   ├── Create: vault.py
│   ├── Build the AlienVault class
│   ├── Add __init__, capture, and __str__
│   └── Run: python3 vault.py
│
├── Activity 2 — Talking to the Alien
│   ├── Update: vault.py
│   ├── Add greet_alien()
│   ├── Test empty and occupied vault responses
│   └── Run: python3 vault.py
│
├── Activity 3 — The Danger of Open Controls
│   ├── Update: vault.py
│   ├── Add public containment attributes
│   ├── Update __str__ to display vault conditions
│   └── Run: python3 vault.py
│
├── Activity 4 — The First Escape
│   ├── Use: vault.py
│   ├── Create: exploit.py
│   ├── Change containment_level directly
│   └── Run: python3 exploit.py
│
├── Activity 5 — Protected Attributes
│   ├── Update: vault.py
│   ├── Rename public controls with one underscore
│   ├── Update __str__ to use protected names
│   └── Run: python3 vault.py
│
├── Activity 6 — The Alien Ignores Warnings
│   ├── Use: vault.py
│   ├── Create: exploit_v2.py
│   ├── Change _containment_level directly
│   └── Run: python3 exploit_v2.py
│
├── Activity 7 — Private Attributes
│   ├── Update: vault.py
│   ├── Replace _containment_level with __containment_level
│   ├── Inspect name mangling with dir()
│   └── Run: python3 vault.py
│
├── Activity 8 — Building the Official Controls
│   ├── Update: vault.py
│   ├── Add reinforce(), weaken(), emergency_lockdown(), and get_status()
│   ├── Keep containment between 0 and 100
│   └── Run: python3 vault.py
│
├── Activity 9 — Alien Communication Console
│   ├── Update: vault.py
│   ├── Add private __responses dictionary
│   ├── Add ask(question)
│   └── Run: python3 vault.py
│
└── Activity 10 — Properties
    ├── Update: vault.py
    ├── Add the containment_level property
    ├── Read the private value through property syntax
    └── Run: python3 vault.py
```

---

## Activity 1 — The Empty Vault

### Script

- Create: `vault.py`
- Run: `python3 vault.py`

### Instructions

1. Create `vault.py`.
2. Define the `AlienVault` class.
3. Add `__init__(self)`.
4. Set `self.occupant` to `None`.
5. Add `capture(self, alien_name)`.
6. Store `alien_name` in `self.occupant`.
7. Add `__str__(self)`.
8. Return the current occupant as a formatted string.
9. Create one `AlienVault` object.
10. Capture `"Gorgax"`.
11. Print the object.
12. Run:

```bash
python3 vault.py
```

---

## Activity 2 — Talking to the Alien

### Script

- Update: `vault.py`
- Run: `python3 vault.py`

### Instructions

1. Pull the latest repository version.
2. Open `vault.py`.
3. Add `greet_alien(self)` inside `AlienVault`.
4. Return an empty-vault message when `self.occupant` is `None`.
5. Return an alien response when an occupant exists.
6. Test the method before capture.
7. Capture `"Gorgax"`.
8. Test the method again.
9. Run:

```bash
python3 vault.py
```

---

## Activity 3 — The Danger of Open Controls

### Script

- Update: `vault.py`
- Run: `python3 vault.py`

### Instructions

1. Pull the latest repository version.
2. Open `vault.py`.
3. Add these public attributes inside `__init__`:
   - `self.containment_level = 100`
   - `self.temperature = 20`
   - `self.oxygen_level = 21`
4. Update `__str__` to display:
   - occupant
   - containment level
   - temperature
   - oxygen level
5. Create and print an occupied vault.
6. Run:

```bash
python3 vault.py
```

---

## Activity 4 — The First Escape

### Scripts

- Use: `vault.py`
- Create: `exploit.py`
- Run: `python3 exploit.py`

### Instructions

1. Pull the latest repository version.
2. Do not change `vault.py`.
3. Create `exploit.py`.
4. Import `AlienVault` from `vault`.
5. Create a vault object.
6. Capture `"Gorgax"`.
7. Print the current vault status.
8. Set `vault.containment_level` directly to `0`.
9. Print the changed vault status.
10. Print an escape message.
11. Run:

```bash
python3 exploit.py
```

---

## Activity 5 — Protected Attributes

### Script

- Update: `vault.py`
- Run: `python3 vault.py`

### Instructions

1. Pull the latest repository version.
2. Open `vault.py`.
3. Rename:
   - `containment_level` to `_containment_level`
   - `temperature` to `_temperature`
   - `oxygen_level` to `_oxygen_level`
4. Update every reference inside `__str__`.
5. Run the script and confirm the values still print.
6. Run:

```bash
python3 vault.py
```

---

## Activity 6 — The Alien Ignores Warnings

### Scripts

- Use: `vault.py`
- Create: `exploit_v2.py`
- Run: `python3 exploit_v2.py`

### Instructions

1. Pull the latest repository version.
2. Do not change `vault.py`.
3. Create `exploit_v2.py`.
4. Import `AlienVault` from `vault`.
5. Create a vault object.
6. Print `vault._containment_level`.
7. Set `vault._containment_level` directly to `0`.
8. Print the new value.
9. Print an escape message.
10. Run:

```bash
python3 exploit_v2.py
```

---

## Activity 7 — Private Attributes

### Script

- Update: `vault.py`
- Run: `python3 vault.py`

### Instructions

1. Pull the latest repository version.
2. Open `vault.py`.
3. Change `_containment_level` to `__containment_level`.
4. Update every internal reference to the new name.
5. Create a vault object.
6. Print the vault.
7. Print `dir(vault)` to inspect the mangled name.
8. Add this test as a comment:

```python
# print(vault.__containment_level)
```

9. Explain that uncommenting it raises `AttributeError`.
10. Run:

```bash
python3 vault.py
```

---

## Activity 8 — Building the Official Controls

### Script

- Update: `vault.py`
- Run: `python3 vault.py`

### Instructions

1. Pull the latest repository version.
2. Open `vault.py`.
3. Add `reinforce(self, amount)`.
4. Increase containment without allowing a value above `100`.
5. Add `weaken(self, amount)`.
6. Decrease containment without allowing a value below `0`.
7. Add `emergency_lockdown(self)`.
8. Set containment directly to `100`.
9. Add `get_status(self)`.
10. Return the current containment level.
11. Update `__str__` to reuse `get_status()`.
12. Test all four methods.
13. Run:

```bash
python3 vault.py
```

---

## Activity 9 — Alien Communication Console

### Script

- Update: `vault.py`
- Run: `python3 vault.py`

### Instructions

1. Pull the latest repository version.
2. Open `vault.py`.
3. Add a private dictionary named `__responses` inside `__init__`.
4. Add responses for:
   - `"hello"`
   - `"escape"`
   - `"name"`
5. Add `ask(self, question)`.
6. Convert the question to lowercase.
7. Check whether a response keyword appears in the question.
8. Return the matching response.
9. Return a default response when no keyword matches.
10. Test three different questions.
11. Run:

```bash
python3 vault.py
```

---

## Activity 10 — Properties

### Script

- Update: `vault.py`
- Run: `python3 vault.py`

### Instructions

1. Pull the latest repository version.
2. Open `vault.py`.
3. Add `@property` above a method named `containment_level`.
4. Return `self.__containment_level`.
5. Update `get_status()` to use `self.containment_level`.
6. Update `__str__` to use `self.containment_level`.
7. Create a vault with an initial containment level of `80`.
8. Print `vault.containment_level` without parentheses.
9. Print the complete vault object.
10. Run:

```bash
python3 vault.py
```

---

## Final Repository Structure

```text
alien-vault/
├── README.md
├── vault.py
├── exploit.py
└── exploit_v2.py
```

## Final Check

Before the lesson ends, confirm that:

- `vault.py` runs successfully.
- `exploit.py` demonstrates the public-attribute failure.
- `exploit_v2.py` demonstrates the protected-attribute failure.
- `vault.py` finishes with private containment data.
- Containment changes only through controlled methods.
- The containment level can be read through `@property`.
- All changes are committed and pushed.
