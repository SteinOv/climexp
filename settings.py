import platform
import os

if platform.system() == 'Darwin':
    # Mac computer
    HOME_DIR = ''
    WORKING_DIR = '/Users/gj/climexp'

    os.environ['PATH'] = '/sw/bin:{WORKING_DIR}/bin:'.format(
       WORKING_DIR=WORKING_DIR) + os.environ['PATH']

    # For NCL
    os.environ['PATH'] = '/usr/local/ncl/bin:' + '/usr/local/bin:' + os.environ['PATH']
    os.environ['NCARG_ROOT'] = '/usr/local/ncl'

else:
    # modern Linux computer
    HOME_DIR = '/home/oldenbor'
    WORKING_DIR = '{HOME_DIR}/climexp'.format(HOME_DIR=HOME_DIR)
    # added /usr/local/bin for the gs that supports transparency, Ubuntu gs does not.
    os.environ['PATH'] = '{HOME_DIR}/bin:{WORKING_DIR}/bin:/usr/local/ncl/bin:/usr/local/bin'.format(
       HOME_DIR=HOME_DIR, 
       WORKING_DIR=WORKING_DIR) + os.environ['PATH']

    # For NCL
    if os.path.isdir("/usr/share/ncarg"):
        os.environ['NCARG_ROOT'] = '/usr/share/ncarg'
    if os.path.isdir("/usr/local/ncl"):
        os.environ['NCARG_ROOT'] = '/usr/local/ncl'

os.chdir(WORKING_DIR)
