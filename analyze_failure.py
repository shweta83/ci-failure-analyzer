import sys
import re
import os

log_file = sys.argv[1] if len(sys.argv) > 1 else "test_output.log"

with open(log_file, "r") as f:
    logs = f.read()

summary = []
summary.append("*** CI Failure Analysis ***")

if "ModuleNotFoundError" in logs:
    match = re.search(r"No module named '(.+?)'", logs)
    if match:
        pkg = match.group(1)
        summary.append(f"Missing dependency: `{pkg}`")
        summary.append(f"Fix: Add `{pkg}` to `requirements.txt`")

    if len(summary) == 1:
        summary.append("Could not identify the exact issue. Check logs")

    output = "\n".join(summary)

# Print in logs
print(output)

# Save to file
with open("failure_summary.md", "w") as f:
    f.write(output)

# Write to GitHub Step Summary (for non-PR runs)
if "GITHUB_STEP_SUMMARY" in os.environ:
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
        f.write(output)