#!c:\micropython\v\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'esptool==2.8','console_scripts','espefuse.py'
__requires__ = 'esptool==2.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('esptool==2.8', 'console_scripts', 'espefuse.py')()
    )
