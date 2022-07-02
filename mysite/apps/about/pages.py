from aquilo import build, div, h1


def page_about():
    root = div(h1("Det här är min Om-sektion"))
    return build(root, title="Om")


def page_projects():
    root = div(h1("Det här är min Projekt-sektion"))
    return build(root, title="Projekt")
