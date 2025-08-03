#!/usr/bin/python3

import os
import json

def load_distro_data(data_path):
    distros = []
    for fname in sorted(os.listdir(data_path)):
        if fname.endswith(".json"):
            with open(os.path.join(data_path, fname)) as f:
                distros.append(json.load(f))
    return distros

def generate_table(versions):
    headers = ["Version", "Codename", "Year", "Based On", "Supported"]
    rows = []

    # Build data rows
    for v in versions:
        row = [
            str(v.get("version", "")),
            str(v.get("codename", "")),
            str(v.get("year", "")),
            str(v.get("based_on", "")),
            "yes" if v.get("supported", False) else "no"
        ]
        rows.append(row)

    # Calculate column widths
    col_widths = [len(header) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))

    # Format row with padding
    def format_row(row):
        return "| " + " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(row)) + " |"

    # Assemble full table
    lines = [
        format_row(headers),
        "|-" + "-|-".join("-" * col_widths[i] for i in range(len(headers))) + "-|"
    ]
    lines.extend(format_row(row) for row in rows)

    return "\n".join(lines)


def generate_readme(distros):
    grouped = {}
    for distro in distros:
        base = distro.get("base") or "Independent"
        grouped.setdefault(base, []).append(distro)

    lines = ["# Linux Distro Base Map", ""]
    for base, children in grouped.items():
        lines.append(f"## Based on: {base}")
        lines.append("")
        for distro in sorted(children, key=lambda d: d["name"]):
            lines.append(f"### {distro['name']}")
            lines.append(f"[{distro['homepage']}]({distro['homepage']})")
            lines.append("")
            lines.append(generate_table(distro.get("versions", [])))
            lines.append("")
    return "\n".join(lines)

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    data_path = os.path.join(script_dir, "..", "data")
    readme_path = os.path.join(script_dir, "..", "README.md")

    distros = load_distro_data(data_path)
    readme_content = generate_readme(distros)

    with open(readme_path, "w") as f:
        f.write(readme_content)
