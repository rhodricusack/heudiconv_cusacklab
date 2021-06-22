import os
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
    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_run-00{item:01d}_T1w')
    func_video = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-video_run-00{item:01d}_bold')
    func_pictures = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-pictures_run-00{item:01d}_bold')

    info = {t1w: [], func_video: [], func_pictures: []}
    
    for idx, s in enumerate(seqinfo):
        if (s.dim1 == 256) and (s.dim2 == 248) and ('t1_mprage_sag_p2' in s.protocol_name):
            info[t1w].append(s.series_id)
        if (s.dim1 == 70) and (s.dim2 == 64) and ('ep2d_bold_moco_s4_post_ch64_VIDEO' in s.protocol_name):
            info[func_video].append(s.series_id)
        if (s.dim1 == 70) and (s.dim2 == 64) and ('ep2d_bold_moco_s4_post_ch64_Pictures' in s.protocol_name):
            info[func_pictures].append(s.series_id)
    print("*********RHODRI")
    print(info)
    return info