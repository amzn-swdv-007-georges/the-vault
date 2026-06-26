# ============================================================
# ROUND 2 - RULES (you CAN edit this file)
#
# Now the system checks a LIST of blocked names before
# deciding whether the person gets on air.
#
# You can only use: variables, lists, for, if / else,
# and a flag variable (blocked = True / False).
# DO NOT use functions (def).
# ============================================================

# Name of the person calling.
caller_name = "VegemiteFan"

# List of names that CANNOT go on air.
blocked_names = ["VegemiteFan", "SpamBot", "TrollGuy"]

# Start by assuming the call is NOT blocked.
blocked = False

# Check the blocked names one by one.
for name in blocked_names:
    if caller_name == name:
        blocked = True

# Final decision.
if blocked:
    on_air = False
else:
    on_air = True
