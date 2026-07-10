import requests

print("=" * 50)
print("CipherGuardian Web Scanner")
print("=" * 50)

target = input("Enter a website (https://example.com): ").strip()

try:
    response = requests.get(target, timeout=10)

    print("\nScan Complete")
    print("-" * 50)
    print("Status Code :", response.status_code)
    print("Server      :", response.headers.get("Server", "Unknown"))
    print("Content-Type:", response.headers.get("Content-Type", "Unknown"))

    print("\nSecurity Headers")

    headers = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    for header in headers:
        if header in response.headers:
            print(f"✓ {header}")
        else:
            print(f"✗ Missing {header}")

except Exception as e:
    print("\nScan failed.")
    print(e)
