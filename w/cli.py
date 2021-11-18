from typing import Optional

import typer

from w import PROGRAM, CLIException
from w.mw_service import MWService

app = typer.Typer()


def _version_cb(value: bool) -> None:
    if value:
        typer.echo(PROGRAM.version_str())
        raise typer.Exit()


_opt_version = typer.Option(False, "--version", "-v", callback=_version_cb, is_eager=True)
_arg_city = typer.Argument(None, help="The city name for checking the weather is rainy or not")


@app.command()
def is_rainy(city_name: str = _arg_city):
    service = MWService()
    try:
        rainy = service.is_rainy(city_name)
        typer.echo("Yes" if rainy else "No")
    except CLIException as e:
        typer.secho(e.args[0], fg=typer.colors.RED, bold=True)
    except BaseException as e:
        typer.secho(e, fg=typer.colors.RED, bold=True)


@app.callback()
def main(version: Optional[bool] = _opt_version) -> None:
    return
