# file_merger
TXT, DAT, and CSV file merger

This script is used to merge multiple files in one folder. User needs to specify folder name,
output filename, and output filetype. Output filetype is optional. If no filetype is provided
the script will check for a filetype in the output filename based on the extension check else
will assign the same extension as that of the first file in the folder.

./merge_file.py -f [FOLDER] -o [OUTPUT_FILENAME] -t [OUTPUT_FILETYPE]
Options:
  -h, --help            show this help message and exit
  -f FOLDER, --folder=FOLDER
                        folder containing files to merge
  -o OUTPUT_FILENAME, --output=OUTPUT_FILENAME
                        output filename
  -t FILETYPE, --type=FILETYPE
                        output filetype. Default filetype is extension of
                        first file in the folder unless specified. Supported
                        filetypes are TXT, CSV, and DAT
