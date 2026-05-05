"""Convert NCV1.json (output of `pdfannots -f json`) into a section-organised
markdown file. Used because the default markdown printer in pdfannots hit an
AssertionError partway through this PDF; the JSON path covers all 48 annots.
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Type → label for the rendered markdown
TYPE_LABEL = {
    "Highlight": "comment",
    "Caret": "insertion / replacement",
    "StrikeOut": "suggested deletion",
    "Text": "sticky note",
    "Underline": "underline",
    "Squiggly": "squiggly",
}

# Annotations before the first prior_outline are in the abstract; assign
# them a virtual section so the grouping works cleanly.
ABSTRACT_OUTLINE = "Abstract / front matter"


def main() -> None:
    with (HERE / "NCV1.json").open() as f:
        annots = json.load(f)

    for a in annots:
        if not a.get("prior_outline"):
            a["prior_outline"] = ABSTRACT_OUTLINE

    # Top-to-bottom: PDF y-coordinate decreases down the page, so sort by -y.
    annots.sort(key=lambda a: (a["page"], -a["start_xy"][1]))

    section_order: list[str] = []
    by_section: dict[str, list[dict]] = {}
    for a in annots:
        s = a["prior_outline"]
        if s not in by_section:
            section_order.append(s)
            by_section[s] = []
        by_section[s].append(a)

    lines: list[str] = []
    lines.append("# Nicola's review — NCV1\n")
    lines.append(f"Source: `specs_2026_op3_loco_study_NCV1.pdf` "
                 f"({len(annots)} annotations across "
                 f"{len(set(a['page'] for a in annots))} pages).\n")
    lines.append("Each entry shows the marked-up text from our manuscript "
                 "(quoted), followed by Nicola's note. Sorted top-to-bottom "
                 "by page.\n")

    for s in section_order:
        lines.append(f"\n## {s}\n")
        for a in by_section[s]:
            label = TYPE_LABEL.get(a["type"], a["type"].lower())
            page = a["page"]
            quoted = (a.get("text") or "").strip()
            note = (a.get("contents") or "").strip()
            # Compact a multi-line quoted span onto one line for readability;
            # multi-line comments keep their structure as a blockquote.
            if quoted:
                quoted = " ".join(quoted.split())
            lines.append(f"- **p{page} · {label}** — “{quoted}”")
            if note:
                for nl in note.splitlines():
                    lines.append(f"  > {nl}" if nl else "  >")
            lines.append("")

    out = HERE / "NCV1-comments.md"
    out.write_text("\n".join(lines))
    print(f"wrote {out}  ({len(annots)} annotations, "
          f"{len(section_order)} sections)")


if __name__ == "__main__":
    main()
