import click

@click.group()
def cli(): pass
@cli.command()
def c1(): click.echo("g2 c1")
@cli.command()
def c2(): click.echo("g2 c1")

if __name__ == "__main__":
    cli()
