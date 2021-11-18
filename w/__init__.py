from dataclasses import dataclass


@dataclass(frozen=True)
class Program:
    app_name: str
    version: str

    def version_str(self):
        return f'{self.app_name} v{self.version}'


class CLIException(Exception):
    pass


PROGRAM = Program(
    app_name='w',
    version='0.0.1'
)

__all__ = (PROGRAM, CLIException, )
