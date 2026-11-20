from pathlib import Path

assets = Path(__file__).resolve().parent

SIMPLE = [
    ("#F8FAFC", "#0B1220"),
    ("#FFFFFF", "#111827"),
    ("#0F172A", "#E2E8F0"),
    ("#64748B", "#94A3B8"),
    ("#E2E8F0", "#1E293B"),
]

sections = [
    "section-about-light-v5.svg",
    "section-stack-light-v5.svg",
    "section-analytics-light-v5.svg",
    "section-projects-light-v5.svg",
    "section-learning-light-v5.svg",
    "footer-light-v5.svg",
]

for name in sections:
    text = (assets / name).read_text(encoding="utf-8")
    for old, new in SIMPLE:
        text = text.replace(old, new)
    out = assets / name.replace("-light-", "-dark-")
    out.write_text(text, encoding="utf-8")
    print("wrote", out.name)

banner = (assets / "banner-light-v5.svg").read_text(encoding="utf-8")
banner_map = [
    ("#FFFFFF", "#0B1220"),
    ("#F8FAFC", "#111827"),
    ("#F1F5F9", "#1E293B"),
    ("#E2E8F0", "#334155"),
    ("#CBD5E1", "#475569"),
    ("#94A3B8", "#64748B"),
    ("#64748B", "#94A3B8"),
    ("#334155", "#CBD5E1"),
    ("#0F172A", "#E2E8F0"),
]
tmp = banner
ph = {}
for i, (old, new) in enumerate(banner_map):
    token = f"__C{i}__"
    ph[token] = new
    tmp = tmp.replace(old, token)
for token, new in ph.items():
    tmp = tmp.replace(token, new)
tmp = tmp.replace('stroke-opacity="0.06"', 'stroke-opacity="0.12"')
out = assets / "banner-dark-v5.svg"
out.write_text(tmp, encoding="utf-8")
print("wrote", out.name)
print("done")
