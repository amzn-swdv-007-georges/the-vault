# Code Hieroglyphics

## The Great Vegemite Call-In War

Work in pairs to modify a Python rules file, test the program, and collaborate using **Git**.

---

## Team Roles

Each team consists of **two students**.

|  Student  |         Role         | Editable Files                       |
| :-------: | :------------------: | :----------------------------------- |
| Student A |   📻 Radio Engineer  | `round1_rules.py`, `round2_rules.py` |
| Student B | 🥪 Vegemite Superfan | `round1_rules.py`, `round2_rules.py` |

Your instructor will provide your private role and objective through **Pumble**.

---

## Setup

Open the **Codio Terminal**.

Clone the repository.

```bash
git clone https://github.com/amzn-swdv-007-georges/call-in-war.git
```

Enter the repository.

```bash
cd call-in-war
```

Navigate to your assigned team directory.

Example:

```bash
cd team-01
```

Verify your location.

```bash
pwd
ls
```

Expected output:

```text
round1_router.py
round1_rules.py
round2_router.py
round2_rules.py
```

---

## Repository Structure

```text
call-in-war/
├── team-01
│   ├── round1_router.py
│   ├── round1_rules.py
│   ├── round2_router.py
│   └── round2_rules.py
├── team-02
│   ├── round1_router.py
│   ├── round1_rules.py
│   ├── round2_router.py
│   └── round2_rules.py
├── team-03
│  ....................
└── team-10
    ├── round1_router.py
    ├── round1_rules.py
    ├── round2_router.py
    └── round2_rules.py
```

Work only inside your assigned team directory.

---

## File Responsibilities

| File               | Action                     |
| ------------------ | -------------------------- |
| `round1_router.py` | Run only. **Do not edit.** |
| `round1_rules.py`  | Edit only.                 |
| `round2_router.py` | Run only. **Do not edit.** |
| `round2_rules.py`  | Edit only.                 |

---

## Git Workflow

Before making any changes, synchronize your local repository.

```bash
git pull
```

### Round 1

Test the program.

```bash
python3 round1_router.py
```

or

```bash
python3 round1_router.py Alice
```

After testing:

```bash
git status
git add round1_rules.py
git commit -m "Update round 1 rule"
git push
```

If `git push` is rejected:

```bash
git pull
python3 round1_router.py
git status
git add round1_rules.py
git commit -m "Update round 1 rule"
git push
```

---

### Round 2

Test the program.

```bash
python3 round2_router.py
```

or

```bash
python3 round2_router.py VegemiteFan
```

After testing:

```bash
git status
git add round2_rules.py
git commit -m "Update round 2 rule"
git push
```

If `git push` is rejected:

```bash
git pull
python3 round2_router.py
git status
git add round2_rules.py
git commit -m "Update round 2 rule"
git push
```

---

## GitHub Authentication

The first time you run `git push`, Codio may request GitHub credentials.

```text
Username: amzn-swdv-007-georges
Password: <Shared GitHub Personal Access Token>
```

Paste the Personal Access Token (PAT) and press **Enter**. The token will not be displayed while you type.

---

## Communication Rules

* Work only inside your assigned team directory.
* Edit only `round1_rules.py` and `round2_rules.py`.
* Never edit `round1_router.py` or `round2_router.py`.
* Test every change before committing.
* Run `git pull` before making changes.
* Keep your private objective confidential.
* Follow only the instructions provided by your instructor through Pumble.
