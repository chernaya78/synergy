import argparse
from jinja2 import Template

FONTS = {
    "roboto": "Roboto, sans-serif",
    "opensans": "'Open Sans', sans-serif",
    "montserrat": "Montserrat, sans-serif",
    "ptsans": "'PT Sans', sans-serif",
    "ubuntu": "Ubuntu, sans-serif"
}

ORG_NAME = "ИП «Чулошников Михаил»"
ORG_DESCRIPTION = """
ИП «Чулошников Михаил» - инновационная компания, занимающаяся разработкой программного обеспечения,
систем машинного обучения и автоматизации бизнес-процессов. Основной офис расположен в Ереване.
"""

def generate_html(font_key: str):
    font_family = FONTS.get(font_key.lower(), FONTS["roboto"])

    with open("template.html", encoding="utf-8") as f:
        template = Template(f.read())

    rendered = template.render(
        font=font_family,
        org_name=ORG_NAME,
        org_description=ORG_DESCRIPTION
    )

    with open("out/index.html", "w", encoding="utf-8") as f:
        f.write(rendered)

    print(f"HTML-страница успешно сгенерирована со шрифтом: {font_key}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генератор HTML-страницы с информацией об организации.")
    parser.add_argument(
        "--font",
        choices=FONTS.keys(),
        default="roboto",
        help=f"Выбор шрифта. Возможные значения: {', '.join(FONTS.keys())}"
    )
    args = parser.parse_args()

    generate_html(args.font)
