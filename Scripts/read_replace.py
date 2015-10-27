"""
Script utile per:
	- copiare un file a chunks a partire da una data stringa
	- fare una replace su delle stringe in un chunk
	- printare a partire da una certa stringa

Usage:
::
	python read_replace.py --function "replace" -i "file_input.txt" -o "file_output.txt" -f "Buongiorno" -r "Buonasera"
	python read_replace.py --function "copy" -i "file_input.txt" -o "file_output.txt" -f "Buongiorno"
	python read_replace.py --function "printer" --find "Buongiorno" -i "file_input.txt"

"""
__author__ = 'davide.cacciavillani@energee3.com'
__reviewer__ = 'alessandro.cucci@energee3.com'

import argparse


def read_in_chunks(file_object, chunk_size=1024):
	"""Lazy function (generator) to read a file piece by piece.
	Default chunk size: 1k."""
	while True:
		data = file_object.read(chunk_size)
		if not data:
			break
		yield data


def readfile(f, string_to_find):
	already_found = False
	for line in f:
		if string_to_find in line or already_found:
			already_found = True
			print line
			raw_input('avanti')


def find_and_replace(file_input, file_output, string_to_find, string_to_replace):
	print file_input, file_output, string_to_find, string_to_replace
	with open(file_input, 'r') as file_in, open(file_output, 'w') as file_out:
		for chunk in read_in_chunks(file_in, 102400):
			chunk = chunk.replace(string_to_find, string_to_replace)
			file_out.write(chunk)


def find_and_print(file_input, string_to_find):
	with open(file_input, 'r') as file_in:
		readfile(file_in, string_to_find)


def find_and_copy(file_input, file_output, string_to_find):
	print file_input, file_output, string_to_find
	start_copy = False
	with open(file_input, 'r') as file_in, open(file_output, 'w') as file_out:
		for chunk in read_in_chunks(file_in):
			if start_copy:
				file_out.write(chunk)
			if string_to_find in chunk:
				start_copy = True
				file_out.write(chunk)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('--function', help='Must be one of "printer", "copy" or "replace"')

	parser.add_argument('--find', '-f', help='string to find')

	parser.add_argument('--replace', '-r', help='string to replace')

	parser.add_argument('--file_input', '-i', help='Input file')

	parser.add_argument('--file_output', '-o', help='Output file')

	args = parser.parse_args()
	if args.function not in ("replace", "printer", "copy"):
		raise ValueError("function not recognised")

	if args.function == "replace":
		find_and_replace(args.file_input, args.file_output, args.find, args.replace)
	elif args.function == "printer":
		find_and_print(args.file_input, args.find)
	elif args.function == "copy":
		find_and_copy(args.file_input, args.file_output, args.find)



