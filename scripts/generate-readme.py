#!/usr/bin/python3

import os
import json

def load_distro_data(data_path):
    distros = []
    for fname in os.listdir(data_path):
        if fname.endswith(".json"):
            with open(os.path.join(data_path, fname)) as f:
                distros.append(json.load(f))
    return distros

def generate_readme(distros):
    grouped = {}
    for distro in distros:
        base = distro["base"] or "Independent"
        grouped.setdefault(base, []).append(distro)

    lines = ["# Linux Distro Base Map", ""]
    for base, children in grouped.items():
        lines.append(f"## Based on: {base}")
        lines.append("")
        for child in sorted(children, key=lambda x: x["name"]):
            lines.append(f"### {child['name']}")
            lines.append(f"- Homepage: [{child['homepage']}]({child['homepage']})")
            lines.append(f"- Versions:")
            for v in child.get("versions", []):
                based = f" (based on {v['based_on']})" if "based_on" in v else ""
                lines.append(f"  - {v['version']} ({v['codename']}, {v['year']}){based}")
            lines.append("")
    return "\n".join(lines)

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    distros = load_distro_data(data_path)
    readme_content = generate_readme(distros)
    with open(os.path.join(os.path.dirname(__file__), "..", "README.md"), "w") as f:
        f.write(readme_content)
