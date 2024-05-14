from IPython.terminal.embed import InteractiveShellEmbed  # noqa: T100


def shell() -> None:
    ipshell = InteractiveShellEmbed()  # noqa: T100
    ipshell.autoawait = True
    ipshell()
