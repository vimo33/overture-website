#!/usr/bin/env python3
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Pitch_Deck"
TARGET = ROOT / "pitch-deck"

SLIDES = [
    ("slide_1_Introduction", "01-introduction.html"),
    ("slide_2_the_crisis_in_local_live_culture", "02-crisis-in-local-live-culture.html"),
    ("slide_3_why_now", "03-why-now.html"),
    ("slide_4_our_solution_updated", "04-our-solution.html"),
    ("slide_5_how_it_works_final", "05-how-it-works.html"),
    ("slide_6_where_we_are_today", "06-where-we-are-today.html"),
    ("slide_7_impact_through_every_subscription_fixed_layout", "07-impact-through-every-subscription.html"),
    ("slide_8_the_zurich_opportunity_updated", "08-the-zurich-opportunity.html"),
    ("slide_9_financial_scenarios_at_chf_20_month", "09-financial-scenarios.html"),
    ("slide_10_venue_participation_model_slide_layout", "10-venue-participation-model.html"),
    ("slide_11_the_pilot_experiment", "11-the-pilot-experiment.html"),
    ("slide_12_fairness_in_practice", "12-fairness-in-practice.html"),
    ("slide_13_proof_matrix", "13-proof-matrix.html"),
    ("slide_14_impact_kpis", "14-impact-kpis.html"),
    ("slide_15_alignment", "15-alignment.html"),
    ("slide_16_the_ask", "16-the-ask.html"),
    ("slide_17_closing", "17-closing.html"),
]


def remove_pattern(html: str, pattern: str) -> str:
    return re.sub(pattern, "", html, flags=re.S)


def add_body_class(html: str, class_name: str) -> str:
    body_with_class = re.sub(
        r'(<body\b[^>]*class=")([^"]*)(")',
        lambda match: f'{match.group(1)}{match.group(2)} {class_name}{match.group(3)}',
        html,
        count=1,
    )
    if body_with_class != html:
        return body_with_class
    return re.sub(r"<body\b", f'<body class="{class_name}"', html, count=1)


def inject_head_assets(html: str) -> str:
    injection = (
        '\n<link rel="stylesheet" href="../assets/css/pitch-deck.css"/>'
        '\n<script defer src="../assets/js/pitch-deck.js"></script>\n'
    )
    if "../assets/css/pitch-deck.css" in html:
        return html
    return html.replace("</head>", injection + "</head>")


def inject_slide_number(html: str, number: int, prev_link: str, next_link: str) -> str:
    marker = (
        f'<a class="deck-index-link" href="./index.html">All Slides</a>\n'
        f'<div class="deck-slide-number">{number:02d}</div>\n'
        f'<a class="deck-hitzone deck-hitzone--prev" data-deck-nav="prev" href="{prev_link or "#"}">Previous slide</a>\n'
        f'<a class="deck-hitzone deck-hitzone--next" data-deck-nav="next" href="{next_link or "#"}">Next slide</a>\n'
    )
    return re.sub(r"(<body\b[^>]*>)", r"\1\n" + marker, html, count=1)


def clean_html(html: str, slide_key: str) -> str:
    html = inject_head_assets(html)
    html = add_body_class(html, "deck-root")
    html = re.sub(r"\n\s*<nav\b.*?</nav>", "", html, flags=re.S)
    html = re.sub(r"\n\s*<button\b.*?</button>", "", html, flags=re.S)
    html = remove_pattern(html, r"\n\s*<div\b[^>]*class=\"[^\"]*\bfixed\b[^\"]*\bbottom[^\"]*\"[^>]*>.*?</div>")
    html = remove_pattern(html, r"\n\s*<footer\b[^>]*class=\"[^\"]*\bfixed\b[^\"]*\bbottom[^\"]*\"[^>]*>.*?</footer>")
    html = remove_pattern(
        html,
        r"\n\s*<!-- Navigation Prompt -->\s*<div class=\"absolute bottom-24 w-full flex justify-center items-center z-20\">.*?</div>\s*</div>",
    )
    html = remove_pattern(html, r"\n\s*<!-- Bottom.*?-->\s*")
    html = remove_pattern(html, r"\n\s*<!-- Visual Slide Accents.*?-->\s*")
    html = re.sub(r"\n\s*<footer\b[^>]*>\s*</footer>", "", html)

    if slide_key == "slide_14_impact_kpis":
      html = remove_pattern(html, r"\n\s*<footer\b.*?</footer>")

    return html


def inject_nav_data(html: str, prev_link: str, next_link: str) -> str:
    return re.sub(
        r"(<body\b)([^>]*)(>)",
        lambda match: (
            f'{match.group(1)}{match.group(2)} data-prev="{prev_link}" data-next="{next_link}"{match.group(3)}'
        ),
        html,
        count=1,
    )


def main() -> None:
    TARGET.mkdir(exist_ok=True)
    for index, (folder, filename) in enumerate(SLIDES, start=1):
        source_file = SOURCE / folder / "code.html"
        html = source_file.read_text(encoding="utf-8")
        html = clean_html(html, folder)
        prev_link = f'./{SLIDES[index - 2][1]}' if index > 1 else ""
        next_link = f'./{SLIDES[index][1]}' if index < len(SLIDES) else ""
        html = inject_nav_data(html, prev_link, next_link)
        html = inject_slide_number(html, index, prev_link, next_link)
        (TARGET / filename).write_text(html, encoding="utf-8")
    print(f"Built {len(SLIDES)} pitch deck slides in {TARGET}")


if __name__ == "__main__":
    main()
