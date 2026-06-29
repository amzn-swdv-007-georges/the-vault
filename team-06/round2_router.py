#!/usr/bin/env python3
import sys

print("====================================================")
print("  RADIO STATION WORKSPACE: LIVE CALL-IN ROUTER v2.0 ")
print("====================================================")


def check_caller(caller_name):
    """
    Execute the student's Round 2 rules and return
    whether the caller is allowed on air.
    """

    # Variables supplied to round2_rules.py
    namespace = {
        "caller_name": caller_name
    }

    try:
        # Execute the student's rules
        with open("round2_rules.py", "r") as rules_file:
            exec(rules_file.read(), namespace)

    except FileNotFoundError:
        print("ERROR: round2_rules.py was not found.")
        return False

    except Exception as e:
        print(f"ERROR while executing round2_rules.py: {e}")
        return False

    # Ensure the student's code created on_air
    if "on_air" not in namespace:
        print("ERROR: round2_rules.py did not set the variable 'on_air'.")
        return False

    allowed = namespace["on_air"]

    if allowed:
        print(f"[+] ACCESS GRANTED: '{caller_name}' is now ON-AIR!")
        print("[*] 'G'day! You're talking to 101.5 FM, what's your Vegemite recipe?'")
    else:
        print(f"[-] ACCESS DENIED: '{caller_name}' was blocked.")
        print("[!] Call routed to pre-recorded loop of elevator music.")

    return allowed


def main():

    print("\nRunning Router Self-Check...\n")

    test_names = [
        "Bruce",
        "Chazza",
        "VegemiteFan",
        "SpamBot",
        "TrollGuy",
        "Dave"
    ]

    for name in test_names:
        print(f"Testing caller: {name}")
        check_caller(name)
        print("-" * 40)

    print("\nInteractive Caller Simulation (Press Ctrl+C to exit)\n")

    try:
        while True:

            caller = input("Enter incoming caller's name: ").strip()

            if caller == "":
                continue

            check_caller(caller)
            print("-" * 40)

    except KeyboardInterrupt:
        print("\nRouter shutting down. Keep those lines clear!")

    except EOFError:
        print("\nInput stream ended.")


if __name__ == "__main__":
    main()