import argparse
import re
import urllib.request

rfcUrl = 'https://tools.ietf.org/rfc/rfc{0}.txt'

parser = argparse.ArgumentParser(description='Download RFC and reformat it for Kindle')
parser.add_argument('rfc', metavar='rfc', type=int, nargs='+', help='A list of RFC numbers to process.')
args = parser.parse_args()

for rfc in args.rfc:
    url = rfcUrl.format(rfc)
    print("Downloading: ", url)
    page = urllib.request.urlopen(url)
    content = str(page.read())
    filename = f'rfc_{rfc}.txt'
    with open(filename, 'w') as file:
        for line in content.split('\\n')[1:]:
            line = line.replace('\\\'', '\'')
            if not(re.match(r'^.*\[Page [0-9]+\]$', line)) and not(re.match(rf'^RFC {rfc}.*$', line)) and not (re.match(r'^\\x0c$', line)):
                file.write(line + '\n')