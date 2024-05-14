from typer import Typer

from src.common.commands import run_server, shell
from src.users.commands import create_admin

commands = (run_server, shell, create_admin)


if __name__ == '__main__':
    typer = Typer()

    for command in commands:
        typer.command()(command)

    typer()
