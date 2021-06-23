# First use of heudiconv on TCIN data

I used the file dicominfo_ses-001.tsv to set up heuristic.py appropriately, but you shouldn't need it now.

Throughout the following, replace [your-study-root] with the where the data will be.

You need docker installed and running.

Copy the dicoms from s3://mrianon and make them into a directory structure like this:
``` bash
[your-study-root]/dicoms/sub-01/ses-001/Series_1_XXX etc
[your-study-root]/dicoms/sub-01/ses-001/Series_2_BLAH etc
```

Then do
``` bash
mkdir -p [your-study-root]/Nifti/code
```
Copy the heuristic.py file from this repository into this folder

``` bash
docker run --rm -it -v [your-study-root]:/base nipy/heudiconv:latest -d /base/dicoms/sub-{subject}/ses-{session}//.dcm -o /base/Nifti/ -f /base/Nifti/code/heuristic.py -s 01 -ss 001 -c dcm2niix -b --overwrite
```
 
One thing that confused me during development: some of the files in /base/Nifti/.heudiconv cause it to cache, so changes to heuristic.py do not get applied. I think due to this:  
  INFO: Reloading existing filegroup.json because /base/Nifti/.heudiconv/01/ses-001/info/01_ses-001.edit.txt exists
To fix this, rm -rf [your-study-root]/Nifti/.heudiconv
