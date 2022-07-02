from aquilo import build, div, h1, a


def page_home():
    root = div(
        [
            h1("Hej, jag heter Vuyo"),
            a("Go to about", href="/about/"),
            a("Go to projects", href="/about/projects/"),
        ]
    )
    return build(root, title="Velkommen til min hemsida")
