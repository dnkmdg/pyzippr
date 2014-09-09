## PyZippr by @foag 2014
## Made to zip files from one path to a combined zip for backup, delivery etc.
## Feel free to use however

from zipfile import ZipFile, ZIP_DEFLATED
from optparse import OptionParser

parser = OptionParser()

## Make options for commandline available through -h

## -f/--files takes a commaseparated list of filenames _without_ paths
parser.add_option("-f", "--files", dest="filename",
                  help="List of files to compress", metavar="FILE")
## -p/--path takes the path for the supplied files
parser.add_option("-p", "--path", dest="path",
                  help="Path containing files", metavar="PATH")
## -o/--outpath takes the path where the zip is to be created
parser.add_option("-o", "--outpath", dest="outpath",
                  help="Outpath", metavar="OUTPATH")
## -z/--zipname takes the filename for the zip file
parser.add_option("-z", "--zipname", dest="zipname",
                  help="Name for zipfile", metavar="ZIPNAME")
(options, args) = parser.parse_args()

with ZipFile(options.outpath+options.zipname,'w',ZIP_DEFLATED) as z:   
  for item in options.filename.split(','):
      print('Crunching '+item)
      z.write(options.path+item,item)
  z.close()
    
print(options.outpath+options.zipname)
    
