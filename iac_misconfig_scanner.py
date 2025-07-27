import os
import re
import sys

# Define rules for detecting misconfigurations
RULES = {
    "Public S3 Bucket": re.compile(r'acl\s*=\s*"(public-read|public-read-write)"', re.IGNORECASE),
    "Open Security Group (Ingress Only)": re.compile(r'ingress\s*{[^}]*?cidr_blocks\s*=\s*\[\s*"0\.0\.0\.0/0"\s*\]',re.IGNORECASE | re.DOTALL),
    "Unencrypted Storage": re.compile(r'resource\s+"aws_ebs_volume".*?[^_]encrypted\s*=\s*false', re.DOTALL | re.IGNORECASE),
    "Disabled CloudTrail": re.compile(r'enable_logging\s*=\s*false', re.IGNORECASE),
    "Over-Permissive IAM Policy": re.compile(r'policy\s*=\s*jsonencode\(\s*{[^}]*?Action\s*=\s*"\*"', re.DOTALL | re.IGNORECASE),
    "Unsecured Endpoint (HTTP)": re.compile(r'http://[^\s"]+', re.IGNORECASE)
}

def scan_file(file_path):
    findings = []
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for rule_name, pattern in RULES.items():
                if pattern.search(content):
                    findings.append(rule_name)
    except Exception as e:
        print(f"[!] Error reading {file_path}: {e}")
    return findings

def scan_directory(root_dir):
    report = {}
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".tf"):
                full_path = os.path.join(subdir, file)
                issues = scan_file(full_path)
                if issues:
                    report[full_path] = issues
    return report

if __name__ == "__main__":
    folder_to_scan = "iac-misconfig-template-dataset"  
    results = scan_directory(folder_to_scan)

    if not results:
        print("No misconfigurations found.")
        sys.exit(0) #Build Sucesss
    else:
        print("Misconfigurations Detected:\n")
        for file_path, issues in results.items():
            print(f"{file_path}")
            for issue in issues:
                print(f"  └─ {issue}")
            print()
        sys.exit(1) #Build Failed

    sys.exit(0)
