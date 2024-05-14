from typer import Typer

from src.users.commands import create_admin

commands = (create_admin,)


if __name__ == '__main__':
    typer = Typer()

    for command in commands:
        typer.command()(command)

    typer()
