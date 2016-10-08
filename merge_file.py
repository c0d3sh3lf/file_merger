#!/usr/bin/python

import optparse, re, os

# Description:
# This script is used to merge multiple files in one folder. User needs to specify folder name,
# output filename, and output filetype. Output filetype is optional. If no filetype is provided
# the script will check for a filetype in the output filename based on the extension check else
# will assign the same extension as that of the first file in the folder.

# Author: Sumit Shrivastava (@invad3rsam)
# Version: v1.0.0


def merge_files(folder, output_filename):
    file_list = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    output_file = open(output_filename, "w")
    for filename in file_list:
        file = open(filename, "r")
        data = file.readlines()
        for line in data:
            output_file.write(line)
        output_file.write(os.linesep)
        file.close()
        print "[+] File '%s' written successfully to '%s'"%(filename, output_filename)
    output_file.close()
    print "[+] All files written to %s"%(output_filename)

def main():
    parser = optparse.OptionParser(usage="./merge_file.py -f [FOLDER] -o [OUTPUT_FILENAME] -t [OUTPUT_FILETYPE]")
    parser.add_option("-f", "--folder", dest="folder", help="folder containing files to merge")
    parser.add_option("-o", "--output", dest="output_filename", help="output filename")
    parser.add_option("-t", "--type", dest="filetype", help="output filetype. Default filetype is extension of first file in the folder unless specified. Supported filetypes are TXT, CSV, and DAT")
    
    has_file_extension = False
    extension = ""

    #Get the user inputs
    (option, args) = parser.parse_args()
    if (option.folder == ""):
        print "[-] Error: Folder required."
        parser.print_help()
        exit(1)
    else:
        folder = option.folder
        if not(os.path.isdir(folder)):
            print "[-] Error: Value is not a valid folder"
            parser.print_help()
            exit(1)
    if (option.output_filename == ""):
        print "[-] Error: Output Filename required."
        parser.print_help()
        exit(1)
    else:
        output_filename = option.output_filename
    if (option.filetype == ""):
        if os.path.isdir(folder):
            for f in os.listdir(folder):
                if os.path.isfile(f):
                    filename_split = f.split(".")
                    extension = filename_split[len(filename_split) - 1]
                    has_file_extension = False
                    break
    else:
        filetype = option.filetype
        if filetype == "TXT" or filetype == "txt":
            file_re = re.compile(r".txt$")
            if file_re.match(output_filename):
                has_file_extension = True
            else:
                has_file_extension = False
                extension = "txt"
        elif filetype == "CSV" or filetype == "csv":
            file_re = re.compile(r".csv$")
            if file_re.match(output_filename):
                has_file_extension = True
            else:
                has_file_extension = False
                extension = "csv"

        elif filetype == "DAT" or filetype == "dat":
            file_re = re.compile(r".dat$")
            if file_re.match(output_filename):
                has_file_extension = True
            else:
                has_file_extension = False
                extension = "dat"
        else:
            print "[-] Invalid file type."
            parser.print_help()
            exit(1)

        if not(has_file_extension):
            output_filename += "." + extension
            merge_files(folder, output_filename)


if __name__ == "__main__":
    main()