joint7_pos = joint7.GetAttribute('physics:localPos0').Get()
joint7_rot = joint7.GetAttribute('physics:localRot1').Get()

data['Joint 7'] = []
data['Joint 7'].append({
    'axis': joint7.GetAttribute('physics:axis').Get(),
    'lower': joint7_lL,
    'pos': [joint7_pos[0], joint7_pos[1], joint7_pos[2]],
    'rot': [joint7_rot.real, joint7_rot.imaginary[0], joint7_rot.imaginary[1], joint7_rot.imaginary[2]],
    'upper': joint7_uL,
    'val': 0,
    'vel': joint7_maxV

})