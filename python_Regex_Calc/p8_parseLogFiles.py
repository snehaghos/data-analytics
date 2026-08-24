# 09. Parse Log Files by Timestamp and Severity
# Level: Intermediate
# Real-Life Scenario
# You are processing an application log. Each line contains a timestamp, severity,
# module, and message. Some messages contain numbers and punctuation.
# Sample Input
# 2026-08-13 10:15:22 [INFO] Auth: Login successful for user=42
# 2026-08-13 10:16:03 [ERROR] DB: Connection failed after 3 retries
# 2026-08-13 10:17:44 [WARN] Cache: Hit ratio below 70%
# 2026-08-13 10:18:01 [INFO] API: Request completed status=200
# Your Tasks
# 48. Parse each log line.
# 49. Capture timestamp, level, module, and message using named groups.
# 50. Find all ERROR entries.
# 51. Count entries by severity.
# 52. Extract the numeric user ID from messages where it exists.
# 53. Make the parser fail safely on a malformed line.

import re
from collections import Counter

LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
    r"\s+\[(?P<level>INFO|ERROR|WARN|DEBUG)\]"
    r"\s+(?P<module>\w+):\s*(?P<message>.+)$",
    re.MULTILINE,
)

USER_ID_PATTERN = re.compile(r"user=(?P<user_id>\d+)")


def problem_08(text):
    """Parse log lines, extract structured data, find errors, count by severity."""
    raw_matches = list(LOG_PATTERN.finditer(text))
    print("Raw matches:")
    for m in raw_matches:
        print(f"  {m.groupdict()}")

    entries = []
    errors = []
    severity_count = Counter()
    user_ids = []

    for m in raw_matches:
        entry = m.groupdict()
        entries.append(entry)
        severity_count[entry["level"]] += 1

        if entry["level"] == "ERROR":
            errors.append(entry)

        uid_match = USER_ID_PATTERN.search(entry["message"])
        if uid_match:
            user_ids.append(int(uid_match.group("user_id")))

    # Test safe failure on malformed lines
    all_lines = text.strip().split("\n")
    malformed = []
    for line in all_lines:
        if line.strip() and not LOG_PATTERN.match(line):
            malformed.append(line)

    print(f"\nMalformed lines: {malformed}")
    print(f"Errors found: {len(errors)}")
    print(f"Severity counts: {dict(severity_count)}")
    print(f"User IDs found: {user_ids}")

    return {
        "entries": entries,
        "errors": errors,
        "severity_count": dict(severity_count),
        "user_ids": user_ids,
        "malformed": malformed,
    }


# --- Test Cases ---

sample = """2026-08-13 10:15:22 [INFO] Auth: Login successful for user=42
2026-08-13 10:16:03 [ERROR] DB: Connection failed after 3 retries
2026-08-13 10:17:44 [WARN] Cache: Hit ratio below 70%
2026-08-13 10:18:01 [INFO] API: Request completed status=200"""

print("Test Case 1: Sample log")
result = problem_08(sample)
print()

test2 = """2026-01-01 00:00:00 [DEBUG] Init: Starting application
2026-01-01 00:00:01 [INFO] Auth: user=101 logged in
2026-01-01 00:00:02 [ERROR] API: Timeout after 30s for user=202
2026-01-01 00:00:03 [ERROR] DB: Deadlock detected
2026-01-01 00:00:04 [WARN] Auth: Failed login attempt for user=999
Some random malformed line without format
2026-01-01 00:00:05 [INFO] Cache: Cleared 500 entries"""

print("Test Case 2: With malformed line and multiple errors")
result2 = problem_08(test2)
print()

test3 = """2025-12-31 23:59:59 [INFO] System: Year-end rollover complete
BROKEN LINE HERE
2025-12-31 23:59:58 [ERROR] DB: Connection pool exhausted"""

print("Test Case 3: Mixed valid and broken")
result3 = problem_08(test3)
print()

test4 = """Just some random text
Another line with numbers 12345
No log format at all"""

print("Test Case 4: All malformed")
result4 = problem_08(test4)
