from aquilo import build, div, h1, a


def page_about():
    root = div(
        [
            h1("Det här är min Om-sektion"), 
            a("Go to home", href="/")
        ]
    )
    return build(root, title="Om")


def page_projects():
    root = div(
        [
            h1("Det här är min Projekt-sektion"),
            a("Go to home", href="/")
        ]
    )
    return build(root, title="Projekt")
