# Clip-Command.py - A multi clipboard program to manage lvm snapshot:

import sys              # Helps to read command line arguments
import pyperclip        # Copy to or paste from clipboard
import datetime         # Work with date and time
import subprocess       # Run shell script or command in python

date = datetime.datetime.now()
formatted_date = date.strftime("%d-%m-%Y")

get_snap_drive = "lsblk | grep 'snap' | head -1 | awk '{print $2}' | sed -e 's/└─//' -e 's/fedora-//' -e 's/--/-/g'"
snap_drive = subprocess.getoutput(get_snap_drive)

COMMANDS = {
    'create': f"sudo lvcreate -L 5GB -s -n root-snap-{formatted_date} /dev/mapper/fedora-root",
    'remove': f"sudo lvremove /dev/fedora/{snap_drive}",
    'merge': f"sudo lvconvert --merge /dev/fedora/{snap_drive}"
}

if len(sys.argv) < 2:
    print('Usage: python 16-Clip-Command.py [kephrase]')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in COMMANDS:
    pyperclip.copy(COMMANDS[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
