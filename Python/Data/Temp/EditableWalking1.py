from App.Proxys import *

data = IKVMCController( 

    name = '',

    controlParamsList = [ 
        ControlParams( joint = 'root', kp = 1000.0, kd = 200.0, tauMax = 200.0, scale = ( 1.0, 1.0, 1.0 ) ),
        ControlParams( 
            joint = 'pelvis_lowerback',
            kp = 75.0,
            kd = 17.3205080757,
            tauMax = 100.0,
            scale = ( 1.0, 1.0, 1.0 ) ),
        ControlParams( joint = 'lowerback_torso', kp = 75.0, kd = 17.3205080757, tauMax = 100.0, scale = ( 1.0, 1.0, 1.0 ) ),
        ControlParams( joint = 'torso_head', kp = 10.0, kd = 6.32455532034, tauMax = 200.0, scale = ( 1.0, 0.2, 1.0 ) ),
        ControlParams( joint = 'lShoulder', kp = 15.0, kd = 7.74596669241, tauMax = 200.0, scale = ( 1.0, 1.0, 1.0 ) ),
        ControlParams( joint = 'rShoulder', kp = 15.0, kd = 7.74596669241, tauMax = 200.0, scale = ( 1.0, 1.0, 1.0 ) ),
        ControlParams( joint = 'lElbow', kp = 5.0, kd = 4.472135955, tauMax = 200.0, scale = ( 0.2, 1.0, 1.0 ) ),
        ControlParams( joint = 'rElbow', kp = 5.0, kd = 4.472135955, tauMax = 200.0, scale = ( 0.2, 1.0, 1.0 ) ),
        ControlParams( joint = 'lHip', kp = 300.0, kd = 34.6410161514, tauMax = 200.0, scale = ( 1.0, 1.0, 1.0 ) ),
        ControlParams( joint = 'rHip', kp = 300.0, kd = 34.6410161514, tauMax = 200.0, scale = ( 1.0, 1.0, 1.0 ) ),
        ControlParams( joint = 'lKnee', kp = 300.0, kd = 34.6410161514, scale = ( 1.0, 1.0, 1.0 ) ),
        ControlParams( joint = 'rKnee', kp = 300.0, kd = 34.6410161514, scale = ( 1.0, 1.0, 1.0 ) ),
        ControlParams( joint = 'lAnkle', kp = 50.0, kd = 14.1421356237, tauMax = 100.0, scale = ( 1.0, 0.2, 0.2 ) ),
        ControlParams( joint = 'rAnkle', kp = 50.0, kd = 14.1421356237, tauMax = 100.0, scale = ( 1.0, 0.2, 0.2 ) ),
        ControlParams( joint = 'lToeJoint', kp = 2.0, kd = 0.2, tauMax = 100.0, scale = ( 1.0, 1.0, 1.0 ) ),
        ControlParams( joint = 'rToeJoint', kp = 2.0, kd = 0.2, tauMax = 100.0, scale = ( 1.0, 1.0, 1.0 ) ) ],

    states = [ 

        SimBiConState( 

            name = 'State 0',

            nextStateIndex = 0,

            duration = 0.59,

            externalForces = [  ],

            trajectories = [ 

                Trajectory( 
                    joint = 'root',
                    strength = [  ],
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 1.0, 0.0 ),
                            reverseOnStance = 'RIGHT',
                            baseTrajectory = [ ( 1.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 0.0, 1.0 ),
                            reverseOnStance = 'RIGHT',
                            baseTrajectory = [ ( 1.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( joint = 'SWING_Hip', strength = [  ], components = [  ] ),

                Trajectory( 
                    joint = 'SWING_Knee',
                    strength = [  ],
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'STANCE_Knee',
                    strength = [  ],
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.2 ), ( 0.5, 0.2 ), ( 1.0, 0.2 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'SWING_Ankle',
                    strength = [  ],
                    referenceFrame = 'CHARACTER_RELATIVE',
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 1.19 ), ( 0.5, 0.315 ), ( 1.0, -0.56 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 0.0, 1.0 ),
                            baseTrajectory = [ ( 0.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'STANCE_Ankle',
                    strength = [  ],
                    referenceFrame = 'CHARACTER_RELATIVE',
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, -0.56 ), ( 0.5, 0.315 ), ( 1.0, 1.19 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 0.0, 1.0 ),
                            reverseOnStance = 'LEFT',
                            baseTrajectory = [ ( 0.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'SWING_Shoulder',
                    strength = [  ],
                    referenceFrame = 'CHARACTER_RELATIVE',
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.4 ), ( 0.5, 0.4 ), ( 1.0, 0.4 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 0.0, 1.0 ),
                            reverseOnStance = 'LEFT',
                            baseTrajectory = [ ( 0.0, -1.5 ), ( 0.5, -1.5 ), ( 1.0, -1.5 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.25 ), ( 0.5, 0.0 ), ( 1.0, -0.25 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'STANCE_Shoulder',
                    strength = [  ],
                    referenceFrame = 'CHARACTER_RELATIVE',
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.4 ), ( 0.5, 0.4 ), ( 1.0, 0.4 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 0.0, 1.0 ),
                            reverseOnStance = 'LEFT',
                            baseTrajectory = [ ( 0.0, 1.5 ), ( 0.5, 1.5 ), ( 1.0, 1.5 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, -0.25 ), ( 0.5, 0.0 ), ( 1.0, 0.25 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'STANCE_Elbow',
                    strength = [  ],
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 1.0, 0.0 ),
                            reverseOnStance = 'LEFT',
                            baseTrajectory = [ ( 0.0, 0.1 ), ( 0.5, 0.1 ), ( 1.0, 0.1 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'SWING_Elbow',
                    strength = [  ],
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 1.0, 0.0 ),
                            reverseOnStance = 'LEFT',
                            baseTrajectory = [ ( 0.0, -0.1 ), ( 0.5, -0.1 ), ( 1.0, -0.1 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'pelvis_lowerback',
                    strength = [  ],
                    referenceFrame = 'CHARACTER_RELATIVE',
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 1.0, 0.0 ),
                            reverseOnStance = 'RIGHT',
                            baseTrajectory = [ ( 0.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 0.0, 1.0 ),
                            reverseOnStance = 'RIGHT',
                            baseTrajectory = [ ( 0.0, 0.0 ), ( 0.5, 0.0 ), ( 1.0, -0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.0 ), ( 0.5, 0.0 ), ( 1.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'lowerback_torso',
                    strength = [  ],
                    referenceFrame = 'CHARACTER_RELATIVE',
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 1.0, 0.0 ),
                            reverseOnStance = 'RIGHT',
                            baseTrajectory = [ ( 0.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 0.0, 1.0 ),
                            reverseOnStance = 'RIGHT',
                            baseTrajectory = [ ( 0.0, 0.0 ), ( 0.5, 0.0 ), ( 1.0, -0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.0 ), ( 0.5, 0.0 ), ( 1.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'torso_head',
                    strength = [  ],
                    referenceFrame = 'CHARACTER_RELATIVE',
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 1.0, 0.0 ),
                            reverseOnStance = 'RIGHT',
                            baseTrajectory = [ ( 0.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 0.0, 0.0, 1.0 ),
                            reverseOnStance = 'RIGHT',
                            baseTrajectory = [ ( 0.0, 0.0 ), ( 0.5, 0.0 ), ( 1.0, -0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ),
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.0 ), ( 0.5, 0.0 ), ( 1.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'SWING_ToeJoint',
                    strength = [ ( 0.3, 0.1 ), ( 0.5, 0.1 ), ( 0.6, 1.0 ) ],
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] ),

                Trajectory( 
                    joint = 'STANCE_ToeJoint',
                    strength = [  ],
                    components = [ 
                        TrajectoryComponent( 
                            rotationAxis = ( 1.0, 0.0, 0.0 ),
                            baseTrajectory = [ ( 0.0, 0.0 ) ],
                            dScaledTrajectory = [  ],
                            vScaledTrajectory = [  ] ) ] )
            ]
        )
    ],

    sagittalTrajectory = [ ( 0.0, 0.0 ), ( 0.5, 0.005 ), ( 1.0, 0.0 ) ],

    coronalTrajectory = [ ( 0.0, 0.0 ), ( 0.5, 0.0 ), ( 1.0, 0.0 ) ],

    heightTrajectory = [ ( 0.0, 0.0 ), ( 0.5, 0.285 ), ( 1.0, 0.0 ) ]
)