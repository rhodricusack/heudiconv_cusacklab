from glob import glob
from heudiconv.cli.run import main
import sys
import glob
import heuristic


files=glob.glob('/mnt/siemens-dicom/anon/ICN_2_RC_FOUNDCOG/*/*/*.dcm')

argv = f'--files {" ".join(files)} -c dcm2niix -o /projects/pi-cusackrh/HPC_18_01039/foundcog/bids/sub-{sub}_ses-{ses} --heuristic /projects/pi-cusackrh/HPC_18_01039/repos/heudiconv_cusacklab/heuristic.py -b --overwrite'.split(' ')

sys.exit(main(argv))
