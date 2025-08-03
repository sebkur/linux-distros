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

def generate_table(versions, include_based_on=True):
    headers = ["Version", "Codename", "Year"]
    if include_based_on:
        headers.append("Based On")
    headers.append("Supported")
    rows = []

    # Build data rows
    for v in versions:
        row = [
            str(v.get("version", "")),
            str(v.get("codename", "")),
            str(v.get("year", "")),
        ]
        if include_based_on:
            row.append(str(v.get("based_on", "")))
        row.append("yes" if v.get("supported", False) else "no")
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

def generate_toc(distros):
    grouped = {}
    for distro in distros:
        base = distro.get("base") or "Independent"
        grouped.setdefault(base, []).append(distro)

    lines = ["## Table of Contents", ""]
    for base in sorted(grouped.keys()):
        base_slug = base.lower().replace(" ", "-")
        if base == "Independent":
            lines.append(f"- [{base}](#{base_slug})")
        else:
            lines.append(f"- [{base}](#based-on-{base_slug})")
        for distro in sorted(grouped[base], key=lambda d: d["name"]):
            distro_slug = distro["name"].lower().replace(" ", "-")
            lines.append(f"  - [{distro['name']}](#{distro_slug})")
    lines.append("")
    return "\n".join(lines)

def generate_readme(distros):
    grouped = {}
    for distro in distros:
        has_base = distro.get("base") is not None
        base = distro.get("base") or "Independent"
        grouped.setdefault(base, []).append(distro)

    lines = []
    for base, children in grouped.items():
        if base == "Independent":
            lines.append(f"## {base}")
        else:
            lines.append(f"## Based on: {base}")
        lines.append("")
        for distro in sorted(children, key=lambda d: d["name"]):
            name = distro["name"]
            has_base = distro.get("base") is not None
            slug = name.lower().replace(" ", "-")
            homepage = distro.get("homepage", "")
            versions = distro.get("versions", [])

            lines.append(f"### {name}")
            if homepage:
                lines.append(f"* Website: [{homepage}]({homepage})")
            lines.append(f"* Standalone file: [distros/{slug}.md](distros/{slug}.md)")
            lines.append("")
            lines.append(generate_table(versions, has_base))
            lines.append("")
    return "\n".join(lines)

def generate_per_distro_pages(distros, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for distro in distros:
        name = distro["name"]
        slug = name.lower().replace(" ", "-")
        homepage = distro.get("homepage", "")
        versions = distro.get("versions", [])

        lines = [f"# {name}", ""]
        if homepage:
            lines.append(f"[{homepage}]({homepage})")
            lines.append("")

        has_base = distro.get("base") is not None
        lines.append(generate_table(versions, has_base))
        lines.append("")

        with open(os.path.join(output_dir, f"{slug}.md"), "w") as f:
            f.write("\n".join(lines))

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    root_dir = os.path.join(script_dir, "..")
    data_path = os.path.join(root_dir, "data")
    distros_path = os.path.join(root_dir, "distros")
    readme_path = os.path.join(root_dir, "README.md")
    preface_path = os.path.join(root_dir, "PREFACE.md")

    distros = load_distro_data(data_path)

    preface = ""
    with open(preface_path, "r") as f:
        preface = f.read().strip() + "\n\n"
    toc = generate_toc(distros) + "\n"

    readme_content = preface + toc + generate_readme(distros)
    with open(readme_path, "w") as f:
        f.write(readme_content)

    generate_per_distro_pages(distros, distros_path)
