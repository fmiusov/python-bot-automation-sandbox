import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:                                                # checks if line is empty or not as a boolean
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)        # calling the main function inside itself (under a condition) is a way to create a loop


def print_line(line, encoding, errors):
    next_lang = line.strip()                                # strips off the \n from the ends, cleans any white space
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)