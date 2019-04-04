import click

from kubetemp import read_params, render_string, write_output


@click.command()
@click.version_option()
@click.argument('TEMPLATE', type=click.File('r'))
@click.option(
    'param_path', '--file', '-f', type=click.Path(exists=True),
    help='Read parameters from JSON or YAML file'
)
@click.option(
    'param_list', '--param', '-p', nargs=2, multiple=True, type=str,
    help='Define parameters to render template'
)
@click.option(
    'output_path', '--output', '-o', type=click.Path(writable=True),
    help='Write rendered template to output file'
)
def cli(template, param_path, param_list, output_path):
    """ Renders Jinja template with parameters"""
    # Get template parameters
    params = {}
    file_params = read_params(param_path)
    params.update(file_params)
    params.update(dict(param_list))

    # Render template and create output
    rendered_output = render_string(template.read(), **params)
    if output_path is None:
        click.echo(rendered_output)
    else:
        write_output(rendered_output, output_path)
