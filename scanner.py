import os
import re

# Define rules for detecting misconfigurations
RULES = {
    "Public S3 Bucket": re.compile(r'acl\s*=\s*"(public-read|public-read-write)"', re.IGNORECASE),
    "Over-Permissive IAM Policy": re.compile(r'"Action"\s*:\s*\[\s*"\*"', re.IGNORECASE),
    "Open Security Group": re.compile(r'cidr_blocks\s*=\s*\[\s*"0\.0\.0\.0/0"\s*\]', re.IGNORECASE),
    "Unencrypted Storage": re.compile(r'resource\s+"aws_ebs_volume".*?[^_]encrypted\s*=\s*false', re.DOTALL | re.IGNORECASE),
    "Unsecured API Gateway": re.compile(r'resource\s+"aws_api_gateway_method".*?authorization\s*=\s*"NONE"', re.DOTALL | re.IGNORECASE),
    "Disabled CloudTrail": re.compile(r'enable_logging\s*=\s*false', re.IGNORECASE),
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
    folder_to_scan = "iac-misconfig-dataset"  # Change if needed
    results = scan_directory(folder_to_scan)

    if not results:
        print("No misconfigurations found.")
    else:
        print("Misconfigurations Detected:\n")
        for file_path, issues in results.items():
            print(f"📄 {file_path}")
            for issue in issues:
                print(f"   └─ {issue}")
            print()
