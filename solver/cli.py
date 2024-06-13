import click

@click.command()
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'))
def cli(input_file, output_file):
    """Process input_file and write output_file"""
    # Read input file
    input_data = input_file.read()

    # Process input data
    processed_data = process_input(input_data)

    # Write processed data to output file
    output_file.write(processed_data)

def process_input(input_data):
    """Process input data"""
    # Add your processing logic here
    return input_data.upper()
