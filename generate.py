from asyncio.windows_events import NULL
from jinja2 import Template, Environment, FileSystemLoader
from playwright.sync_api import sync_playwright
from needs import element
from sort import generate_result


def get_result():
    pass


def generate_html(result: element):
    jin_env = Environment(loader=FileSystemLoader("./web", encoding="utf-8"))
    template = jin_env.get_template("index.html")
    output = template.render(
        fivestar=result.fivestar,
        sixgold=result.sixgold,
        ground=result.ground,
        family=result.family,
        info=result.info,
        name=result.name,
    )
    with open("./web/output.html", "w", encoding="utf-8") as f:
        f.write(output)
        f.close()


def generate_picture():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        file_path = "D:\code\python\predic\web\output.html"
        page.goto(file_path)
        page.screenshot(path="D:\code\python\predic\web\output.png")
        context.close()
        browser.close()
