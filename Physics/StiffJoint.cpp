#include "StiffJoint.h"

#include <Physics/ArticulatedRigidBody.h>

StiffJoint::StiffJoint(){
}

StiffJoint::~StiffJoint(void){
}


/**
	This method is used to fix the joint angular constraint to correct for drift. This is done by changing
	the orientation of the child.
*/
void StiffJoint::fixAngularConstraint(const Quaternion& qRel){
	//not much to do here...
}

