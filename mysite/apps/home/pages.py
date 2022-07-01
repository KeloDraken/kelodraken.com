from aquilo import build, div, h1


def page_home():
    root = div(h1("Hej, jag heter Vuyo"))
    return build(root, title="Velkommen til min hemsida")
