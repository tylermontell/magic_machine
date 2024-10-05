import os
import re

# Path to the repopack output file
REPOPACK_FILE = "repopack-output.xml"
OUTPUT_FILE = "optimized-repopack-output.xml"
IGNORE_PATTERNS = ['*.log', '*.test', 'tmp/', 'node_modules/', 'venv/', '__pycache__']

# Convert glob patterns to regex for `should_ignore` function
def glob_to_regex(pattern):
    return re.sub(r"\*", r".*", pattern)

def should_ignore(file_path):
    # Convert glob patterns to regex
    patterns_to_ignore = [glob_to_regex(p) for p in IGNORE_PATTERNS]
    
    for pattern in patterns_to_ignore:
        try:
            if re.search(pattern, file_path):
                return True
        except re.error as e:
            print(f"Invalid regex pattern '{pattern}': {e}")
            continue
    return False

def extract_summaries(lines):
    """Extract summaries and return them as a list."""
    summary_section = []
    for line in lines:
        if "<summary>" in line:
            summary_section.append(line)
    return summary_section

def reorder_critical_sections(lines):
    """Reorder critical sections like summaries and config files at the top."""
    critical_sections = []
    remaining_lines = []
    for line in lines:
        if "<summary>" in line or "README" in line or "config.py" in line:
            critical_sections.append(line)
        else:
            remaining_lines.append(line)
    return critical_sections + remaining_lines

def preprocess_repopack_output():
    """Main function to preprocess repopack output file."""
    with open(REPOPACK_FILE, 'r') as f:
        lines = f.readlines()

    # Step 1: Filter out ignored files
    cleaned_lines = [line for line in lines if not should_ignore(line)]

    # Step 2: Extract summaries
    summaries = extract_summaries(cleaned_lines)

    # Step 3: Reorder critical sections
    reordered_lines = reorder_critical_sections(cleaned_lines)

    # Step 4: Write the optimized output
    with open(OUTPUT_FILE, 'w') as f:
        f.write("<!-- Session Summaries -->\n")
        f.writelines(summaries)
        f.write("<!-- Remaining Content -->\n")
        f.writelines(reordered_lines)

    print(f"Optimized repopack output written to {OUTPUT_FILE}")

if __name__ == "__main__":
    preprocess_repopack_output()
