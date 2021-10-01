import os
from os import path

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes
def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where
    allowed template fields - follow python string module:
    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """
    anat = create_key('anat/sub-{subject}_{session}_run-00{item:01d}_T1w')
    func_video = create_key('func/sub-{subject}_{session}_dir-AP_task-videos_run-00{item:01d}_bold')
    func_pictures = create_key('func/sub-{subject}_{session}_dir-AP_task-pictures_run-00{item:01d}_bold')
    func_rest5 = create_key('func/sub-{subject}_{session}_dir-AP_task-rest5_run-00{item:01d}_bold')
    func_rest10 = create_key('func/sub-{subject}_{session}_dir-AP_task-rest10_run-00{item:01d}_bold')
    dwi = create_key('dwi/sub-{subject}_{session}_dir-{dir}_run-{item}_dwi')
    fmap = create_key('fmap/sub-{subject}_{session}_dir-{dir}_run-{item}_epi')
    info = {anat: [], func_video: [], func_pictures: [], func_rest5: [], func_rest10: [], dwi: [], fmap:[] }
    
    for idx, s in enumerate(seqinfo):
        if 't2_tse_tra_p3_noisereduction' in s.protocol_name:
            info[anat].append(s.series_id)
        if (s.dim1 == 64) and (s.dim2 == 64) and ('cmrr_mbep2d_bold_videos_AP' in s.protocol_name):
            info[func_video].append(s.series_id)
        if (s.dim1 == 64) and (s.dim2 == 64) and ('cmrr_mbep2d_bold_Pictures_AP' in s.protocol_name):
            info[func_pictures].append(s.series_id)
        if (s.dim1 == 64) and (s.dim2 == 64) and ('cmrr_mbep2d_bold_Resting_10' in s.protocol_name):
            info[func_rest10].append(s.series_id)
        if (s.dim1 == 64) and (s.dim2 == 64) and ('cmrr_mbep2d_bold_Resting_5' in s.protocol_name):
            info[func_rest5].append(s.series_id)
        if (s.dim1 == 96) and (s.dim2 == 96) and ('cmrr_mbep2d_diff_AP_mb4_norm_pulse1.5x' in s.protocol_name):
            info[dwi].append({'item': s.series_id, 'dir':'AP'})
        if (s.dim1 == 96) and (s.dim2 == 96) and ('cmrr_mbep2d_diff_PA_mb4_norm_pulse1.5x' in s.protocol_name):
            info[dwi].append({'item': s.series_id, 'dir':'PA'})
        if (s.dim1 == 64) and (s.dim2 == 64) and ('cmrr_mbep2d_se_AP' in s.protocol_name):
            info[fmap].append({'item': s.series_id, 'dir':'AP'})
        if (s.dim1 == 64) and (s.dim2 == 64) and ('cmrr_mbep2d_se_PA' in s.protocol_name):
            info[fmap].append({'item': s.series_id, 'dir':'PA'})

    print('*** infotodict')
    print(info)

    return info

# Get a numeric subject ID for BIDS format from list of DICOM file names
def infotoids(seqinfos, outdir):
    # Use the sub and ses labels as given in the output path
    fp = outdir.split(path.sep)
    if fp[-1][:4] == 'ses-':
        ses=fp[-1][4:]
    if fp[-2][:4] == 'sub-':
        sub=fp[-2][4:]
    
    return({'subject':sub, 'session':ses, 'locator':outdir})