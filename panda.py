# System
import numpy as np
import json

# USD
from pxr import Usd, Vt

data = {}
stage = Usd.Stage.Open('franka.usda')
panda = stage.GetPrimAtPath('/panda')

n_dof = 7
links = []
joints = []
visuals = []
joint_uL = []
joint_lL = []
joint_maxV = []


for i in range(n_dof+1):
    link_name = '/panda/panda_link' + str(i)
    joint_name = link_name + '/panda_joint' + str(i+1)
    visual_name = link_name + '/visuals'
    links.append(stage.GetPrimAtPath(link_name))
    joints.append(stage.GetPrimAtPath(joint_name))
    visuals.append(stage.GetPrimAtPath(visual_name))

    joint_lL.append(joints[i].GetAttribute('physics:lowerLimit').Get())
    joint_uL.append(joints[i].GetAttribute('physics:upperLimit').Get())
    joint_maxV.append(joints[i].GetAttribute('physxJoint:maxJointVelocity').Get())

    joint_pos = joints[i].GetAttribute('physics:localPos0').Get()
    joint_rot = joints[i].GetAttribute('physics:localRot1').Get()
    faceVertexIndices = np.array(visuals[i].GetAttribute('faceVertexIndices').Get()).tolist()
    normals = np.array(visuals[i].GetAttribute('normals').Get()).tolist()
    points = np.array(visuals[i].GetAttribute('points').Get()).tolist()

    data['Link ' + str(i)] = []
    data['Link ' + str(i)].append({
        'faceVertexIndices':faceVertexIndices,
        'points':points
    })

    data['Joint ' + str(i)] = []
    data['Joint ' + str(i)].append({
        'axis': joints[i].GetAttribute('physics:axis').Get(),
        'lower': joint_lL[i],
        'pos': [joint_pos[0], joint_pos[1], joint_pos[2]],
        'rot': [joint_rot.real,joint_rot.imaginary[0], joint_rot.imaginary[1], joint_rot.imaginary[2]],
        'upper': joint_uL[i],
        'val': 0,
        'vel': joint_maxV[i],
    })


with open('panda.json', 'w') as outfile:
    json.dump(data, outfile, indent =2)

print("panda.json file generated!")