#!/usr/bin/env python3
import sys

def evaluate_caller(caller_name):
    """
    Executes the student's routing rules and returns
    whether the caller is allowed on air.
    """

    # Variables made available to round1_rules.py
    namespace = {
        "caller_name": caller_name
    }

    # Execute the student's rules
    with open("round1_rules.py", "r") as f:
        exec(f.read(), namespace)

    # Read the student's decision
    return namespace["on_air"]


def main():
    print("====================================================")
    print("  RADIO STATION WORKSPACE: LIVE CALL-IN ROUTER v1.0 ")
    print("====================================================\n")

    if len(sys.argv) > 1:
        caller = " ".join(sys.argv[1:])
        print(f"Testing Caller: {caller}")

        allowed = evaluate_caller(caller)

        if allowed:
            print(f"Result: [ ALLOWED ] - {caller} is now LIVE on the airwaves!")
        else:
            print(f"Result: [ BLOCKED ] - Call from {caller} was rejected.")
    else:
        try:
            while True:
                caller = input("Enter caller name (or Ctrl+C to exit): ").strip()

                if not caller:
                    continue

                allowed = evaluate_caller(caller)

                if allowed:
                    print(f"--> [ ALLOWED ] - {caller} is on the air!\n")
                else:
                    print(f"--> [ BLOCKED ] - {caller} was routed to voicemail.\n")

        except KeyboardInterrupt:
            print("\nExiting Router. Have a great broadcast!")


if __name__ == "__main__":
    main()