import flet 
from flet import Page, Text

def main(page: Page):
    t = Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

flet.app(port= 8656,target=main, view=flet.WEB_BROWSER)
# flet.app(target=main, view=flet.DESKTOP) bu kod ile web browser görünümüne geçebilirsiniz.