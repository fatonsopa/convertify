from convertify import Convertify
import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("--source", required=False,help="Source path of images", type=str)
ap.add_argument("--destination", help="Destination path of images", type=str)
ap.add_argument("--from",  help="Type of the image to convert from", type=str)
ap.add_argument("--to",  help="Type of the image to convert to", default="webp", type=str)
ap.add_argument("--r",  help="Run the script recursively", default=True, type=bool)

args = vars(ap.parse_args())

def main():
    Convertify.convert(source_path=args['source'],
              destination_path=args['destination'],
              from_type=args['from'],
              to_type=args['to'],
              recursive=args['r']
  )