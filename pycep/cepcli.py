"""The pycep cli python package."""
# coding=utf-8
import click
import ujson

from logging import DEBUG, ERROR, basicConfig, info

from pycep import __version__
from pycep.parse import open_input_file
from pycep.plugin import linter, markdown_out, spellcheck, package_info, sentiment_analyzer, return_non_data_slide, \
    markdown_in, package_questions


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
@click.option("--input_file", "-f", help="The Package export tar.gz or the json file .")
@click.option("--file_type", "-t", help="Input File type format json/tar.gz.", default="tar")
@click.option("--output", "-o", help="Output file directory.")
@click.option("--word_list", "-w", help="Input spelling word list.", default="pycep/data/word_list.txt")
@click.option("--plugin", "-p", help="Plugin for pycep to run.", required=True)
@click.option("--input_directory", "-g", help="The Package export directory that generates a package export tar.gz or "
                                              "the json file ")
@click.option('--debug/', "-d",  help="Turn debug mode on.",
              is_flag=True, callback=cli, expose_value=False, is_eager=True, default=False)
@click.option('--version', help="Print Application Version",
              is_flag=True, callback=print_version, expose_value=False, is_eager=True)
@click.option("--export-dir", "-e", help="Export file directory.", envvar='EXPORT_DIR')
@click.option("--owner-id", "-uid", help="User account UID.", envvar='OWNER_ID')
def pycep_cli(input_file, plugin, file_type, output, word_list, input_directory, export_dir, owner_id):
    """Pycep Command line interface."""
    if input_file:
        input_data = ujson.loads(open_input_file(input_file, file_type))
    else:
        input_data = None
    if "linter" == plugin:
        info("pycep linter plugin running now...")
        linter(input_data)

    elif "render" == plugin:
        info("pycep render plugin running now...")
        markdown_out(input_data, output)

    elif "spellcheck" == plugin:
        info("pycep render plugin running now...")
        spellcheck(input_data, word_list)

    elif "packageinfo" == plugin:
        info("pycep package_info plugin running now...")
        package_info(input_data)

    elif "nltk" == plugin:
        info("pycep nltk plugin running now...")
        sentiment_analyzer(input_data)
    elif "question" == plugin:
        tester = package_questions(input_data)
        print()
    elif "generate" == plugin:
        markdown_in(output, input_directory, export_dir, owner_id)


if __name__ == '__main__':
    pycep_cli()
