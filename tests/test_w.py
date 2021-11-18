from typer.testing import CliRunner

from w import PROGRAM, cli


runner = CliRunner()


def test_version():
    result = runner.invoke(cli.app, ['--version'])
    assert result.exit_code == 0
    assert f"{PROGRAM.version_str()}" in result.stdout
    result = runner.invoke(cli.app, ['-v'])
    assert result.exit_code == 0
    assert f"{PROGRAM.version_str()}" in result.stdout


def test_is_rainy():
    result = runner.invoke(cli.app, ['is-rainy', 'not-city'])
    assert result.exit_code == 0
    assert "The city cannot found 'not-city'" in result.stdout
