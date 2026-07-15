import subprocess

tests = [
    "tests.test_memory",
    "tests.test_intent",
    "tests.test_knowledge",
    "tests.test_feedback",
    "tests.test_history",
    "tests.test_brain"
]

print("=" * 35)
print("      Sepehr Test Suite")
print("=" * 35)

passed = 0

for test in tests:

    print(f"\nRunning {test} ...")

    result = subprocess.run(
        ["python", "-m", test]
    )

    if result.returncode == 0:
        passed += 1

print("\n" + "=" * 35)
print(f"TOTAL : {passed}/{len(tests)} PASS")
print("=" * 35)
