"""The pycep python cli python package."""
# coding=utf-8
import click
import json

from logging import DEBUG, ERROR, basicConfig, info

from pycep import __version__
from pycep.parser import open_input_file
from pycep.plugin import linter, markdown_out, spellcheck


def value_check(value, ctx):
    """Return boolean result from ctx parsing."""
    if not value or ctx.resilient_parsing:
        return True
    return False


def cli(ctx, param, debug):
    """Set command line debug level output to stdout."""
    if value_check(debug, ctx):
        return
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))
    if debug:
        logging_level = DEBUG
        log_format = 'Process Time: %(asctime)s | %(message)s'
    else:
        logging_level = ERROR
        log_format = '%(message)s'
    basicConfig(level=logging_level, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')


def print_version(ctx, param, value):
    """Print pycep version to stdout."""
    if value_check(value, ctx):
        return
    click.echo(str(__version__))
    ctx.exit()


@click.command()
@click.option("--input_file", "-f", help="The Package export tar.gz or the json file .", required=True)
@click.option("--file_type", "-t", help="Input File type format json/tar.gz.", default="tar")
@click.option("--output", "-o", help="Output file directory.")
@click.option("--word_list", "-w", help="Input spelling word list.", default="pycep/data/word_list.txt")
@click.option("--plugin", "-p", help="Plugin for pycep to run.", required=True)
@click.option('--debug/', "-d",  help="Turn debug mode on.",
              is_flag=True, callback=cli, expose_value=False, is_eager=True, default=False)
@click.option('--version', help="Print Application Version",
              is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def pycep_cli(input_file, plugin, file_type, output, word_list):
    """Pycep Command line interface."""
    input_data = json.loads(open_input_file(input_file, file_type))
    if "linter" == plugin:
        info("pycep linter plugin running now...")
        linter(input_data)

    elif "render" == plugin:
        info("pycep render plugin running now...")
        markdown_out(input_data, output)

    elif "spellcheck" == plugin:
        info("pycep render plugin running now...")
        spellcheck(input_data, word_list)


if __name__ == '__main__':
    pycep_cli()
