# Run heudiconv with
docker run --rm -it -v /home/cusackrh/mrianon/:/base nipy/heudiconv:latest -d /base/sub-{subject}/ses-{session}/*/*.dcm -o /base/Nifti/ -f /base/Nifti/code/heuristic.py -s 01 -ss 001 -c dcm2niix -b --overwrite
