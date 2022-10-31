import flet 
from flet import Page, Text

def main(page: Page):
    t = Text(
    value="This is a Text control sample",
    size=30,
    color="white",
    bgcolor="pink",
    weight="bold",
    italic=True,)
    
    page.controls.append(t)
    page.update()

flet.app(port= 8656,target=main, view=flet.WEB_BROWSER)
# flet.app(target=main, view=flet.DESKTOP) bu kod ile web browser görünümüne geçebilirsiniz. Ve target öncesine port tanımlayadabiliriz.