import click
import sudoku_parser 

@click.group()
def cli():
    """Sudoku solver CLI"""
    pass

@cli.command()
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'), default=None)
def solve(input_file: str, output_file: str | None = None):
    """Solve input_file and write to output_file"""
    # Read input file
    input_data = input_file.read()

    sudoku_parser.parse_sudoku(input_data)

    # Process input data
    #processed_data = process_input(input_data)

    # Write processed data to output file
    #output_file.write(processed_data)

def process_input(input_data):
    """Process input data"""
    # Add your processing logic here
    return input_data.upper()

if __name__ == '__main__':
    cli()