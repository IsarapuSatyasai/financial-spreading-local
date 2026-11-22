def get_user_prompt(metrics: list) -> str:
    lines = []
    current = None
    for m in metrics:
        if m["worksheet"] != current:
            current = m["worksheet"]
            lines.append(f"\n### Table: {current}")
        desc = m.get("description") or ""
        lines.append(f"- Variable: '{m['variable']}' (Description: {desc})")
    return "\n".join(lines)
