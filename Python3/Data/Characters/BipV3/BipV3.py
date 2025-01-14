'''
Created on 2009-08-28

@author: beaudoin
'''

from os import path

meshDir = path.join( path.dirname(__file__), "Meshes" ) 
blue  = ( 0.5, 0.6, 0.8, 1 )
green = ( 0.5, 0.8, 0.6, 1 )
red   = ( 0.892, 0.716, 0.602, 1 )
gray  = ( 0.5, 0.5, 0.5, 1 )

from App.Proxys import *

data = Character(
                         
    name = "BipV3",
                         
    root = ArticulatedRigidBody(
        name = "pelvis",
        meshes = [ (path.join(meshDir, "pelvis.obj"), blue) ],
        mass = 12.9,
        moi = (0.0705, 0.11, 0.13),
        cdps = [ CapsuleCDP((-0.05, -0.025, 0), (0.05, -0.025, 0), 0.07) ],
        pos = (0, 1.035, 0),
        frictionCoeff = 0.8,
        restitutionCoeff = 0.35 ),
    
    arbs = [
        ArticulatedRigidBody(
            name = "lowerBack",
            meshes = [ (path.join(meshDir, "lowerBack.obj"), green) ],
            mass = 7.0,
            moi = (0.1, 0.08, 0.15),
            cdps = [ CapsuleCDP((0,-0.05,0), (0, 0.015, 0), 0.08) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),

        ArticulatedRigidBody(
            name = "torso",
            meshes = [ (path.join(meshDir, "torso.obj"), green) ],
            mass = 15.5,
            moi = (0.21, 0.14, 0.31),
            cdps = [ CapsuleCDP((0, -0.05, 0.03), (0, 0.07, 0.03), 0.12) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),
    
        ArticulatedRigidBody(
            name = "head",
            meshes = [ (path.join(meshDir, "head.obj"), red) ],
            mass = 5.2,
            moi = (0.04, 0.02, 0.042),
            cdps = [ CapsuleCDP((0,0.05,0), (0,0.1,0), 0.09) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),
            
        ArticulatedRigidBody(
            name = "lUpperArm",
            meshes = [ (path.join(meshDir, "lUpperArm.obj"), green) ],
            mass = 2.2,
            moi = (0.005, 0.02, 0.02),
            cdps = [ CapsuleCDP((-0.13,0,0), (0.08,0,0), 0.04) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),
            
        ArticulatedRigidBody(
            name = "lLowerArm",
            meshes = [ (path.join(meshDir, "lLowerArm.obj"), red) ],
            mass = 1.7,
            moi = (0.0024, 0.025, 0.025),
            cdps = [ CapsuleCDP((-0.2,0,0), (0.07,0,0), 0.04) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),
        
        ArticulatedRigidBody(
            name = "rUpperArm",
            meshes = [ (path.join(meshDir, "rUpperArm.obj"), green) ],
            mass = 2.2,
            moi = (0.005, 0.02, 0.02),
            cdps = [ CapsuleCDP((0.13,0,0), (-0.08,0,0), 0.04) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),

        ArticulatedRigidBody(
            name = "rLowerArm",
            meshes = [ (path.join(meshDir, "rLowerArm.obj"), red) ],
            mass = 1.7,
            moi = (0.0024, 0.025, 0.025),
            cdps = [ CapsuleCDP((-0.07,0,0), (0.2,0,0), 0.04) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),
        
        ArticulatedRigidBody(
            name = "lUpperLeg",
            meshes = [ (path.join(meshDir, "lUpperLeg.obj"), blue) ],
            mass = 6.6,
            moi = (0.15, 0.022, 0.15),
            cdps = [ CapsuleCDP((0, 0.15, 0), (0, -0.19, 0), 0.05) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),

        ArticulatedRigidBody(
            name = "lLowerLeg",
            meshes = [ (path.join(meshDir, "lLowerLeg.obj"), blue) ],
            mass = 3.2,
            moi = (0.055, 0.007, 0.055),
            cdps = [ CapsuleCDP((0, 0.17, 0), (0, -0.22, 0), 0.05) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),

        ArticulatedRigidBody(
            name = "rUpperLeg",
            meshes = [ (path.join(meshDir, "rUpperLeg.obj"), blue) ],
            mass = 6.6,
            moi = (0.15, 0.022, 0.15),
            cdps = [ CapsuleCDP((0, 0.15, 0), (0, -0.19, 0), 0.05) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),

        ArticulatedRigidBody(
            name = "rLowerLeg",
            meshes = [ (path.join(meshDir, "rLowerLeg.obj"), blue) ],
            mass = 3.2,
            moi = (0.055, 0.007, 0.055),
            cdps = [ CapsuleCDP((0, 0.17, 0), (0, -0.22, 0), 0.05) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35 ),

        ArticulatedRigidBody(
            name = "lFoot",
            meshes = [ (path.join(meshDir, "lFoot.obj"), gray) ],
            mass = 1.0,
            moi = (0.007, 0.008, 0.002),
            cdps = [ BoxCDP((-0.05, -0.04, -0.09), (0.05, 0.005, 0.065)) ], 
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35,
            groundCoeffs = (0.0005, 0.2) ),

        ArticulatedRigidBody(
            name = "rFoot",
            meshes = [ (path.join(meshDir, "rFoot.obj"), gray) ],
            mass = 1.0,
            moi = (0.007, 0.008, 0.002),
            cdps = [ BoxCDP((-0.05, -0.04, -0.09), (0.05, 0.005, 0.065)) ], 
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35,
            groundCoeffs = (0.0005, 0.2) ),
            
        ArticulatedRigidBody(
            name = "lToes",
            meshes = [ (path.join(meshDir, "lToes.obj"), gray) ],
            mass = 0.2,
            moi = (0.002, 0.002, 0.0005),
            cdps = [ BoxCDP((-0.03, 0.015, -0.035), (0.03, -0.017, 0.02)) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35,
            groundCoeffs = (0.0005, 0.2) ),
            
        ArticulatedRigidBody(
            name = "rToes",
            meshes = [ (path.join(meshDir, "rToes.obj"), gray) ],
            mass = 0.2,
            moi = (0.002, 0.002, 0.0005),
            cdps = [ BoxCDP((-0.03, 0.015, -0.035), (0.03, -0.017, 0.02)) ],
            frictionCoeff = 0.8,
            restitutionCoeff = 0.35,
            groundCoeffs = (0.0005, 0.2) )
    ],
    
    joints = [
                   
        BallInSocketJoint(
            name = "pelvis_lowerback",
            parent = "pelvis",
            child = "lowerBack",
            posInParent = (0, 0.07, -0.015),
            posInChild = (0, -0.09, -0.015),
            swingAxis1 = (1, 0, 0),
            twistAxis = (0, 0, 1),
            limits = (-0.6, 0.6, -0.6, 0.6, -0.6, 0.6) ),
        
        BallInSocketJoint(
            name = "lowerback_torso",
            parent = "lowerBack",
            child = "torso",
            posInParent = (0, 0.05, -0.015),
            posInChild = (0, -0.138, 0.012),
            swingAxis1 = (1, 0, 0),
            twistAxis = ( 0, 0, 1),
            limits = (-0.6, 0.6, -0.6, 0.6, -0.6, 0.6) ),
        
        BallInSocketJoint(
            name = "torso_head",
            parent = "torso",
            child = "head",
            posInParent = (0, 0.16, 0.00),
            posInChild = (0, -0.08, -0.03),
            swingAxis1 = (1, 0, 0),
            twistAxis = ( 0, 0, 1),
            limits = (-0.6, 0.6, -0.6, 0.6, -0.6, 0.6) ),
        
        BallInSocketJoint(
            name = "lShoulder",
            parent = "torso",
            child = "lUpperArm",
            posInParent = (0.16, 0.095, 0.02),
            posInChild = (-0.13, 0, 0),
            swingAxis1 = (0, 0, 1),
            twistAxis = ( 1, 0, 0),
            limits = (-100, 100, -1.5, 1.5, -100, 100) ),
        
        BallInSocketJoint(
            name = "rShoulder",
            parent = "torso",
            child = "rUpperArm",
            posInParent = (-0.16, 0.095, 0.02),
            posInChild = (0.13, 0, 0),
            swingAxis1 = (0, 0, 1),
            twistAxis = ( 1, 0, 0),
            limits = (-100, 100, -1.5, 1.5, -100, 100) ),
                    
        HingeJoint(
            name = "lElbow",
            parent = "lUpperArm",
            child = "lLowerArm",
            posInParent = (0.11, 0, 0),
            posInChild = (-0.24, 0, 0),
            axis = ( 0, 1, 0 ),
            limits = (-2.7, 0) ),
        
        HingeJoint(
            name = "rElbow",
            parent = "rUpperArm",
            child = "rLowerArm",
            posInParent = (-0.11, 0, 0),
            posInChild = (0.24, 0, 0),
            axis = ( 0, -1, 0 ),
            limits = (-2.7, 0) ),
        
        BallInSocketJoint(
            name = "lHip",
            parent = "pelvis",
            child = "lUpperLeg",
            posInParent = (0.08, -0.03, -0.01),
            posInChild = (0, 0.17, 0),
            swingAxis1 = (1, 0, 0),
            twistAxis = ( 0, 0, 1),
            limits = (-1.3, 1.9, -1, 1, -1, 1) ),
        
        BallInSocketJoint(
            name = "rHip",
            parent = "pelvis",
            child = "rUpperLeg",
            posInParent = (-0.08, -0.03, -0.01),
            posInChild = (0, 0.17, 0),
            swingAxis1 = (1, 0, 0),
            twistAxis = ( 0, 0, 1),
            limits = (-1.3, 1.9, -1, 1, -1, 1) ),
            
        HingeJoint(
            name = "lKnee",
            parent = "lUpperLeg",
            child = "lLowerLeg",
            posInParent = (0, -0.23, 0),
            posInChild = (0, 0.22, 0),
            axis = ( 1, 0, 0 ),
            limits = (0, 2.5) ),
            
        HingeJoint(
            name = "rKnee",
            parent = "rUpperLeg",
            child = "rLowerLeg",
            posInParent = (0, -0.23, 0),
            posInChild = (0, 0.22, 0),
            axis = ( 1, 0, 0 ),
            limits = (0, 2.5) ),
            
        
        UniversalJoint(
            name = "lAnkle",
            parent = "lLowerLeg",
            child = "lFoot",
            posInParent = (0.01, -0.24, 0.00),
            posInChild = (0.0, 0.02, -0.03),
            parentAxis = (0, 0, 1),
            childAxis = (1, 0, 0),
            limits = (-0.75, 0.75, -0.75, 0.75) ),
        
        UniversalJoint(
            name = "rAnkle",
            parent = "rLowerLeg",
            child = "rFoot",
            posInParent = (-0.01, -0.24, 0.00),
            posInChild = (0.0, 0.02, -0.03),
            parentAxis = (0, 0, -1),
            childAxis = (1, 0, 0),
            limits = (-0.75, 0.75, -0.75, 0.75) ),
            
        HingeJoint(
            name = "lToeJoint",
            parent = "lFoot",
            child = "lToes",
            posInParent = (0, -0.02, 0.055),
            posInChild = (0, 0, -0.045),
            axis = ( 1, 0, 0 ),
            limits = (-0.52, 0.1) ),
            
        HingeJoint(
            name = "rToeJoint",
            parent = "rFoot",
            child = "rToes",
            posInParent = (0, -0.02, 0.055),
            posInChild = (0, 0, -0.045),
            axis = ( 1, 0, 0 ),
            limits = (-0.52, 0.1) )
    ]
)

