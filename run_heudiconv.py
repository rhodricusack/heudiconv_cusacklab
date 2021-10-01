from heudiconv import bids
from heudiconv.main import workflow
from os import path

import glob

# Path to scan
dcmpth='/mnt/siemens-dicom/anon'

# Each subject
allsubjdicom = glob.glob(path.join(dcmpth,'*_RC_FOUNDCOG'))
for subjdicom in allsubjdicom:
    flds = path.basename(subjdicom).split('_') 
    # bids descriptor for this subject
    sub = ''.join(flds[:2]) # removed _ (e.g., ICN_2 -> ICN2) as underscore typically splits fields in bids

    # Each session for this subject
    allsessdicom = glob.glob(subjdicom+'/*')
    allsessdicom.sort() # sessions in ascending order by time

    for ses, sessdicom in enumerate(allsessdicom, start = 1):
        print(f'Working on sub-{sub} ses-{ses}')

        files = glob.glob(path.join(sessdicom,'*/*.dcm'))

        workflow(files=files, 
            converter='dcm2niix',
            outdir=f'/projects/pi-cusackrh/HPC_18_01039/foundcog/bids/sub-{sub}/ses-{ses}',
            heuristic='/projects/pi-cusackrh/HPC_18_01039/repos/heudiconv_cusacklab/heuristic.py',
            overwrite=True, 
            bids_options=[])
