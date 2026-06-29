import sys

# ==============================================================================
# VEGEMITE CALL-IN WAR: ROUND 2 ROUTER
# ==============================================================================
# Radio Engineers (Student A): Add more names to this list or make the loop strict.
# Vegemite Superfans (Student B): Remove names from this list or bypass the loop!
# ==============================================================================
blocklist = ["Bruce", "Sheila", "VegemiteLover"]

print("--- STATION 101.5 FM: VEGEMITE CALL-IN WAR ROUTER v2.0 ---")
print(f"Active Blocklist: {blocklist}\n")

def check_caller(caller_name):  
    cleaned_caller = caller_name.strip()
    is_blocked = False
    
    # Loop through blocklist to inspect each blocked name
    for blocked_name in blocklist:
        if cleaned_caller.lower() == blocked_name.lower():
            is_blocked = True
            break
            
    if is_blocked:
        print(f"[-] ACCESS DENIED: '{caller_name}' is on the blocklist!")
        print("[!] Call routed to pre-recorded loop of elevator music.")
        return False
    else:
        print(f"[+] ACCESS GRANTED: '{caller_name}' is now ON-AIR!")
        print("[*] 'G'day! You're talking to 101.5 FM, what's your Vegemite recipe?'")
        return True

# If run directly, allow entering names
if __name__ == "__main__":
    print("Running Router Self-Check...")
    test_names = ["Bruce", "Chazza", "VegemiteLover", "Dave"]
    for name in test_names:
        print(f"Testing caller: {name}")
        check_caller(name)
        print("-" * 40)
        
    print("\nInteractive Caller Simulation (Press Ctrl+C to exit):")
    try:
        while True:
            caller = input("Enter incoming caller's name: ")
            if not caller:
                break
            check_caller(caller)
            print("-" * 40)
    except KeyboardInterrupt:
        print("\nRouter shutting down. Keep those lines clear!")
    except EOFError:
        print("\nInput stream ended.")
