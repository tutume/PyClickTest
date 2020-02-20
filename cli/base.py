import click

@click.group()
def cli(): pass

@cli.group()
def g1(): pass
@g1.command()
def c1(): print("g1 c1")
@g1.command()
def c2(): print("g1 c1")

@cli.group()
def g2(): pass
@g2.command()
def c1(): print("g2 c1")
@g2.command()
def c2(): print("g2 c1")

if __name__ == "__main__":
    cli()
