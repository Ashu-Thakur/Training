import sys

# it provide a list that contains all the arguments ,first value always gonna be the script name
args = sys.argv
print(args[1:])

# !----------------argparser
import argparse

# Example script (script.py)
if __name__ == "__main__":
   parse = argparse.ArgumentParser(description="Parsing the arguments getting from terminal")
   parse.add_argument("first",type=str , help="this is positional argument")
   parse.add_argument("--second",default="",type=str , help="this is optional argument") #convention to use -- for optional argemnts name
   parse.add_argument("third",type=str , help="this is positional argument")

   args = parse.parse_args()
   print(args.first)
   print(args.second)
   print(args.third)
   print(args)

# !argsparse is provide more control over args
# !we can set optional and positional arguments
# !description and help just for printing purpose when we use to run this scripts with postfix -h
# !the order is followed by position arguments not optional we can pass optional by giving their and then their values in any order

#? Positional Arguments: Identified by their position, always required, cannot be passed by name.
#? Optional Arguments: Identified by flags (e.g., --arg1), can be optional or required, can be passed by name.