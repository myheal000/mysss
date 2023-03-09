_base_ = './faster_rcnn_orpn_r50_fpn_3x_hrsc.py'
model = dict(
    backbone=dict(
        dcn=dict(type='DCN', deformable_groups=1, fallback_on_stride=False),
        stage_with_dcn=(True, True, True, True)))
