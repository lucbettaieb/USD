from pxr import Usd, Vt
import json

data = {}
stage = Usd.Stage.Open('franka.usda')
panda = stage.GetPrimAtPath('/panda')

link0 = stage.GetPrimAtPath('/panda/panda_link0')
joint1 = stage.GetPrimAtPath('/panda/panda_link0/panda_joint1')

link1 = stage.GetPrimAtPath('/panda/panda_link1')
joint2 = stage.GetPrimAtPath('/panda/panda_link1/panda_joint2')

link2 = stage.GetPrimAtPath('/panda/panda_link2')
joint3 = stage.GetPrimAtPath('/panda/panda_link2/panda_joint3')

link3 = stage.GetPrimAtPath('/panda/panda_link3')
joint4 = stage.GetPrimAtPath('/panda/panda_link3/panda_joint4')

link4 = stage.GetPrimAtPath('/panda/panda_link4')
joint5 = stage.GetPrimAtPath('/panda/panda_link4/panda_joint5')

link5 = stage.GetPrimAtPath('/panda/panda_link5')
joint6 = stage.GetPrimAtPath('/panda/panda_link5/panda_joint6')

link6 = stage.GetPrimAtPath('/panda/panda_link6')
joint7 = stage.GetPrimAtPath('/panda/panda_link6/panda_joint7')

link7 = stage.GetPrimAtPath('/panda/panda_link7')
joint8 = stage.GetPrimAtPath('/panda/panda_link7/panda_joint8')

link8 = stage.GetPrimAtPath('/panda/panda_link8')
hand_joint = stage.GetPrimAtPath('/panda/panda_link8/panda_hand_joint')

hand = stage.GetPrimAtPath('/panda/panda_hand')
finger_joint1 = stage.GetPrimAtPath('/panda/panda_hand/panda_finger_joint1')
finger_joint2 = stage.GetPrimAtPath('/panda/panda_hand/panda_finger_joint2')

print(joint1.GetPropertyNames())

#Joint Limits
joint1_uL = joint1.GetAttribute('physics:upperLimit').Get()
joint1_lL = joint1.GetAttribute('physics:lowerLimit').Get()
joint2_uL = joint2.GetAttribute('physics:upperLimit').Get()
joint2_lL = joint2.GetAttribute('physics:lowerLimit').Get()
joint3_uL = joint3.GetAttribute('physics:upperLimit').Get()
joint3_lL = joint3.GetAttribute('physics:lowerLimit').Get()
joint4_uL = joint4.GetAttribute('physics:upperLimit').Get()
joint4_lL = joint4.GetAttribute('physics:lowerLimit').Get()
joint5_uL = joint5.GetAttribute('physics:upperLimit').Get()
joint5_lL = joint5.GetAttribute('physics:lowerLimit').Get()
joint6_uL = joint6.GetAttribute('physics:upperLimit').Get()
joint6_lL = joint6.GetAttribute('physics:lowerLimit').Get()
joint7_uL = joint7.GetAttribute('physics:upperLimit').Get()
joint7_lL = joint7.GetAttribute('physics:lowerLimit').Get()
# joint8_uL = joint8.GetAttribute('physics:upperLimit').Get()
# joint8_lL = joint8.GetAttribute('physics:lowerLimit').Get()


data['limits'] = []
data['limits'].append([[joint1_lL, joint1_uL],
                      [joint2_lL, joint2_uL],
                      [joint3_lL, joint3_uL],
                      [joint4_lL, joint4_uL],
                      [joint5_lL, joint5_uL],
                      [joint6_lL, joint6_uL],
                      [joint7_lL, joint7_uL]])
                    #   [joint8_lL, joint8_uL]])


#DOF

data['num_dof'] = 7

#Max Velocity

joint1_maxV = joint1.GetAttribute('physxJoint:maxJointVelocity').Get()
joint2_maxV = joint2.GetAttribute('physxJoint:maxJointVelocity').Get()
joint3_maxV = joint3.GetAttribute('physxJoint:maxJointVelocity').Get()
joint4_maxV = joint4.GetAttribute('physxJoint:maxJointVelocity').Get()
joint5_maxV = joint5.GetAttribute('physxJoint:maxJointVelocity').Get()
joint6_maxV = joint6.GetAttribute('physxJoint:maxJointVelocity').Get()
joint7_maxV = joint7.GetAttribute('physxJoint:maxJointVelocity').Get()

data['max_velocity'] = []
data['max_velocity'].append([joint1_maxV,
                             joint2_maxV,
                             joint3_maxV,
                             joint4_maxV,
                             joint5_maxV,
                             joint6_maxV,
                             joint7_maxV])

#Joint1

joint1_pos = joint1.GetAttribute('physics:localPos0').Get()
joint1_rot = joint1.GetAttribute('physics:localRot1').Get()

data['Joint 1'] = []
data['Joint 1'].append({
    'axis': joint1.GetAttribute('physics:axis').Get(),
    'lower': joint1_lL,
    'pos': [joint1_pos[0], joint1_pos[1], joint1_pos[2]],
    'rot': [joint1_rot.real, joint1_rot.imaginary[0], joint1_rot.imaginary[1], joint1_rot.imaginary[2]],
    'upper': joint1_uL,
    'val': 0,
    'vel': joint1_maxV

})

#Joint2

joint2_pos = joint2.GetAttribute('physics:localPos0').Get()
joint2_rot = joint2.GetAttribute('physics:localRot1').Get()

data['Joint 2'] = []
data['Joint 2'].append({
    'axis': joint2.GetAttribute('physics:axis').Get(),
    'lower': joint2_lL,
    'pos': [joint2_pos[0], joint2_pos[1], joint2_pos[2]],
    'rot': [joint2_rot.real, joint2_rot.imaginary[0], joint2_rot.imaginary[1], joint2_rot.imaginary[2]],
    'upper': joint2_uL,
    'val': 0,
    'vel': joint2_maxV

})

#Joint3

joint3_pos = joint3.GetAttribute('physics:localPos0').Get()
joint3_rot = joint3.GetAttribute('physics:localRot1').Get()

data['Joint 3'] = []
data['Joint 3'].append({
    'axis': joint3.GetAttribute('physics:axis').Get(),
    'lower': joint3_lL,
    'pos': [joint3_pos[0], joint3_pos[1], joint3_pos[2]],
    'rot': [joint3_rot.real, joint3_rot.imaginary[0], joint3_rot.imaginary[1], joint3_rot.imaginary[2]],
    'upper': joint3_uL,
    'val': 0,
    'vel': joint3_maxV

})

#Joint4

joint4_pos = joint4.GetAttribute('physics:localPos0').Get()
joint4_rot = joint4.GetAttribute('physics:localRot1').Get()

data['Joint 4'] = []
data['Joint 4'].append({
    'axis': joint4.GetAttribute('physics:axis').Get(),
    'lower': joint4_lL,
    'pos': [joint4_pos[0], joint4_pos[1], joint4_pos[2]],
    'rot': [joint4_rot.real, joint4_rot.imaginary[0], joint4_rot.imaginary[1], joint4_rot.imaginary[2]],
    'upper': joint4_uL,
    'val': 0,
    'vel': joint4_maxV

})

#Joint5

joint5_pos = joint5.GetAttribute('physics:localPos0').Get()
joint5_rot = joint5.GetAttribute('physics:localRot1').Get()

data['Joint 5'] = []
data['Joint 5'].append({
    'axis': joint5.GetAttribute('physics:axis').Get(),
    'lower': joint5_lL,
    'pos': [joint5_pos[0], joint5_pos[1], joint5_pos[2]],
    'rot': [joint5_rot.real, joint5_rot.imaginary[0], joint5_rot.imaginary[1], joint5_rot.imaginary[2]],
    'upper': joint5_uL,
    'val': 0,
    'vel': joint5_maxV

})


#Joint6

joint6_pos = joint6.GetAttribute('physics:localPos0').Get()
joint6_rot = joint6.GetAttribute('physics:localRot1').Get()

data['Joint 6'] = []
data['Joint 6'].append({
    'axis': joint6.GetAttribute('physics:axis').Get(),
    'lower': joint6_lL,
    'pos': [joint6_pos[0], joint6_pos[1], joint6_pos[2]],
    'rot': [joint6_rot.real, joint6_rot.imaginary[0], joint6_rot.imaginary[1], joint6_rot.imaginary[2]],
    'upper': joint6_uL,
    'val': 0,
    'vel': joint6_maxV

})

#Joint7

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


mass = link0.GetAttribute('physics:mass')
inertia = link0.GetAttribute('physics:diagonalInertia')

# print(mass.Get())
# print(inertia.Get())

# print("Position", joint1.GetAttribute('physics:localPos1').Get())

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent =2)
