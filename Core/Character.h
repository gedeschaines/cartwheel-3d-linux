#pragma once

#include <Physics/PhysicsGlobals.h>
#include <Physics/ArticulatedFigure.h>
#include <Utils/Utils.h>
#include "SimGlobals.h"

class ReducedCharacterStateArray : public DynamicArray<double> {
};


/**
	A character is an articulated figure - This class implements methods that allow it to easily save and restore its state, etc.
*/
class Character : public ArticulatedFigure {
	friend class SimBiController;
	friend class Controller;
	friend class IKVMCController;
	friend class VirtualModelController;
	friend class TestApp;
	friend class TestApp2;
	friend class BehaviourController;

private:
	/**
		this method is used to rotate the character about the vertical axis, so that its heading has the value that is given as a parameter.
		It is assumed that the quaternion passed in here represents a rotation about the vertical axis - that's why it is a private method
	*/
	void setHeading(Quaternion heading);

	/**
		this method is used to rotate the character (well, the character whose state is passed in as a parameter)
		about the vertical axis, so that it's default heading has the value that is given as a parameter.
	*/
	void setHeading(Quaternion heading, ReducedCharacterStateArray* state, int start = 0);


	// Hack! This is for backward compatibility with previous formats that had the joints ordered in this way.
	DynamicArray<int> jointOrder;
	DynamicArray<int> reverseJointOrder;
	void updateJointOrdering();

public:
	/**
		the constructor
	*/
	Character();

	/**
		the destructor
	*/
	~Character(void);

	/**
		This method is used to populate the relative orientation of the parent and child bodies of joint i.
	*/
	void getRelativeOrientation(int i, Quaternion* qRel);

	/**
		This method is used to get the relative angular velocities of the parent and child bodies of joint i,
		expressed in parent's local coordinates.
	*/
	void getRelativeAngularVelocity(int i, Vector3d* wRel);


	/**
		this method is used to read the reduced state of the character from the file, into the array passed in as a parameter. The
		state of the character is not modified
	*/
	void readReducedStateFromFile(char* fName, ReducedCharacterStateArray* state);

	/**
		this method is used to read the reduced state of the character from the file
	*/
	void loadReducedStateFromFile(char* fName);

	/**
		this method is used to write the reduced state of the character to a file
	*/
	void saveReducedStateToFile(char* fName);

	/**
		this method is used to write the reduced state of the character to a file
	*/
	void saveReducedStateToFile(char* fName, ReducedCharacterStateArray& state);

	/**
		This method populates the dynamic array passed in with the state of the character.
		For the state, we consider the 13-dimensional state of the root, and then only
		the relative orientation and angular velocity (as measured in parent coordinates) for
		every other link. The velocities of the CM are derived from this information,
		using the velocity propagation technique (if that's what it is called).
		The order in which the bodies appear is given by the array of joints.
		This works under the assumption that in the joint
		sequence, the parent of any rigid body appears before its children (assuming that for each joint
		we read the parent first and then the child).
	*/
	void getState(ReducedCharacterStateArray* state);

	/**
		This method populates the state of the current character with the values that are passed
		in the dynamic array. The same conventions as for the getState() method are assumed.
		We'll assume that the index of the first state variable in the state array is given by
		'start'.
	*/
	void setState(ReducedCharacterStateArray* state, int start = 0, bool hackFlag = true);

	/**
		This method returns the dimension of the state. Note that we will consider
		each joint as having 3-DOFs (represented by the 4 values of the quaternion)
		without taking into account what type of joint it is (i.e. a hinge joint
		has only one degree of freedom, but we will still consider the relative orientation
		of the child relative to the parent as a quaternion.
	*/
	int getStateDimension();

	/**
		this method is used to return the current heading of the character
	*/
	Quaternion getHeading();

	/**
		this method is used to return the current heading of the character, specified as an angle measured in radians
	*/
	double getHeadingAngle();

	/**
		this method is used to rotate the character about the vertical axis, so that it's default heading has the value that is given as a parameter
	*/
	void setHeading(double val);

	/* Recenter the character at 0,0 on the x,z plane */
	void recenter();

	/**
		this method is used to rotate the character (well, the character whose state is passed in as a parameter)
		about the vertical axis, so that it's default heading has the value that is given as a parameter
	*/
	void setHeading(double val, ReducedCharacterStateArray* state, int start = 0);

	/**
		this method takes the state of the character, passed in as an array of doubles, and reverses it inplace
	*/
	void reverseStanceOfStateArray(ReducedCharacterStateArray* state, int start = 0);

	/**
		this method is used to retrieve the reduced state of the character, but with the stance reversed.
	*/
	void getReverseStanceState(ReducedCharacterStateArray* state);

	/**
		This method is used to compute the center of mass of the articulated figure.
	*/
	Vector3d getCOM();

	/**
		This method is used to compute the velocity of the center of mass of the articulated figure.
	*/
	Vector3d getCOMVelocity();

};

#define REDUCED_STATE_VAL(CHAR_STATE, I) ((*((CHAR_STATE)->state))[(I)])


/**
	This method decomposes the rotation that is passed in into a rotation by the vertical axis - called vertical twist or heading, and everything else:
	rot = qHeading * qOther;
	The returned orientation is qHeading.
*/
inline Quaternion computeHeading(const Quaternion& rot){
	return rot.getComplexConjugate().decomposeRotation(PhysicsGlobals::up).getComplexConjugate();
}


//a useful structure that holds information regarding which joints are relevant for the distance measure, and how much they're worth
typedef struct {
	//this is the index of the joint, as it appears in the reduced state
	int jIndex;
	//this is how much the difference in the relative orientations should be worth
	double wQ;
	//and this is how much the difference in the relative angular velocity should be worth
	double wV;
} RelevantJoint;

/**
	This class is used to map the array of doubles that is used to define the state of the character to an
	easier to use and understand meaning of the state. This should be the only place in the code where we need to know
	that the first 13 numbers in the array represent the position, orientation, velocity and angular velocity, etc.
*/
class ReducedCharacterState{
private:
	DynamicArray<double>* state;
	int startIndex;
public:
	/**
		Constructor. Allows the index in the array of doubles to be specified as well.
	*/
	ReducedCharacterState(DynamicArray<double>* s, int index = 0){
		state = s;
		this->startIndex = index;
	}

	/**
		Destructor - not much to do here.
	*/
	~ReducedCharacterState(){
	}

	/**
		gets the root position.
	*/
	inline Vector3d getPosition(){
		return Vector3d(REDUCED_STATE_VAL(this, 0+startIndex), REDUCED_STATE_VAL(this, 1+startIndex), REDUCED_STATE_VAL(this, 2+startIndex));
	}

	/**
		sets the root position.
	*/
	inline void setPosition(const Vector3d& p){
		REDUCED_STATE_VAL(this, 0 + startIndex) = p.x;
		REDUCED_STATE_VAL(this, 1 + startIndex) = p.y;
		REDUCED_STATE_VAL(this, 2 + startIndex) = p.z;
	}

	/**
		gets the root orientation.
	*/
	inline Quaternion getOrientation(){
		return Quaternion(REDUCED_STATE_VAL(this, 3+startIndex), REDUCED_STATE_VAL(this, 4+startIndex), REDUCED_STATE_VAL(this, 5+startIndex),  REDUCED_STATE_VAL(this, 6+startIndex));
	}

	/**
		sets the root orientation.
	*/
	inline void setOrientation(const Quaternion& q){
		REDUCED_STATE_VAL(this, 3 + startIndex) = q.s;
		REDUCED_STATE_VAL(this, 4 + startIndex) = q.v.x;
		REDUCED_STATE_VAL(this, 5 + startIndex) = q.v.y;
		REDUCED_STATE_VAL(this, 6 + startIndex) = q.v.z;
	}

	/**
		gets the root velocity.
	*/
	inline Vector3d getVelocity(){
		return Vector3d(REDUCED_STATE_VAL(this, 7+startIndex), REDUCED_STATE_VAL(this, 8+startIndex), REDUCED_STATE_VAL(this, 9+startIndex));
	}

	/**
		sets the root velocity.
	*/
	inline void setVelocity(const Vector3d& v){
		REDUCED_STATE_VAL(this, 7 + startIndex) = v.x;
		REDUCED_STATE_VAL(this, 8 + startIndex) = v.y;
		REDUCED_STATE_VAL(this, 9 + startIndex) = v.z;
	}

	/**
		gets the root angular velocity.
	*/
	inline Vector3d getAngularVelocity(){
		return Vector3d(REDUCED_STATE_VAL(this, 10+startIndex), REDUCED_STATE_VAL(this, 11+startIndex), REDUCED_STATE_VAL(this, 12+startIndex));
	}

	/**
		sets the root angular velocity.
	*/
	inline void setAngularVelocity(const Vector3d& v){
		REDUCED_STATE_VAL(this, 10 + startIndex) = v.x;
		REDUCED_STATE_VAL(this, 11 + startIndex) = v.y;
		REDUCED_STATE_VAL(this, 12 + startIndex) = v.z;
	}

	/**
		gets the relative orientation for joint jIndex
	*/
	inline Quaternion getJointRelativeOrientation(int jIndex){
		int offset = startIndex + 13 + 7 * jIndex;
		return Quaternion(REDUCED_STATE_VAL(this, 0 + offset), REDUCED_STATE_VAL(this, 1 + offset), REDUCED_STATE_VAL(this, 2 + offset),  REDUCED_STATE_VAL(this, 3 + offset));
	}

	/**
		sets the orientation for joint jIndex
	*/
	inline void setJointRelativeOrientation(const Quaternion& q, int jIndex){
		int offset = startIndex + 13 + 7 * jIndex;
		REDUCED_STATE_VAL(this, 0 + offset) = q.s;
		REDUCED_STATE_VAL(this, 1 + offset) = q.v.x;
		REDUCED_STATE_VAL(this, 2 + offset) = q.v.y;
		REDUCED_STATE_VAL(this, 3 + offset) = q.v.z;
	}

	/**
		gets the relative angular velocity for joint jIndex
	*/
	inline Vector3d getJointRelativeAngVelocity(int jIndex){
		int offset = startIndex + 13 + 7 * jIndex;
		return Vector3d(REDUCED_STATE_VAL(this, 4 + offset), REDUCED_STATE_VAL(this, 5 + offset), REDUCED_STATE_VAL(this, 6 + offset));
	}

	/**
		sets the orientation for joint jIndex
	*/
	inline void setJointRelativeAngVelocity(const Vector3d& w, int jIndex){
		int offset = startIndex + 13 + 7 * jIndex;
		REDUCED_STATE_VAL(this, 4 + offset) = w.x;
		REDUCED_STATE_VAL(this, 5 + offset) = w.y;
		REDUCED_STATE_VAL(this, 6 + offset) = w.z;
	}




	/**
		this method can be used to compute the distance between two reduced character states that both belong to the raptor model.
	*/
	inline double raptor_computeDistanceTo(ReducedCharacterState *other){
		//these are the settings for bip3Dv3...
		//the joints are: body_neck, lHip, rHip, lKnee, rKnee, neck_head, tail_1
		RelevantJoint joints[] = {{0, 1.5, 1}, {1, 1.5, 0.1}, {2, 1.5, 0.1}, {7, 1, 0.05}, {8, 1, 0.05}, {6, 1.5, 0.05}, {5, 1, 0.05}};
		double result = 0;
		Quaternion qa, qb;
		Vector3d va, vb;

		//for the root orientation only consider the heading independent orientation
		qa = computeHeading(this->getOrientation()).getComplexConjugate() * this->getOrientation();
		qb = computeHeading(other->getOrientation()).getComplexConjugate() * other->getOrientation();

		va = this->getOrientation().getComplexConjugate().rotate(this->getVelocity());
		vb = other->getOrientation().getComplexConjugate().rotate(other->getVelocity());

		result += 3 * distanceBetweenOrientations(qa, qb);
		result += 3 * (va-vb).dotProductWith(va-vb);

		//and now penalize the difference in root angular velocities
		va = this->getOrientation().getComplexConjugate().rotate(this->getAngularVelocity());
		vb = other->getOrientation().getComplexConjugate().rotate(other->getAngularVelocity());
		result += 3 * (va-vb).dotProductWith(va-vb);

		//now go through all the joints that are relevant, and penalize the differences in the orientations and angular velocities
		for (uint i=0;i<sizeof(joints)/sizeof(joints[1]);i++){
			qa = this->getJointRelativeOrientation(joints[i].jIndex);
			qb = other->getJointRelativeOrientation(joints[i].jIndex);
			va = this->getJointRelativeAngVelocity(joints[i].jIndex);
			vb = other->getJointRelativeAngVelocity(joints[i].jIndex);
			result += joints[i].wQ * distanceBetweenOrientations(qa, qb);
			result += joints[i].wV * (va-vb).dotProductWith(va-vb);
		}

		return result;
	}

	/**
		this method can be used to compute the distance between two reduced character states that both belong to the bip3dv3 model.
	*/
	inline double bigBird3d_computeDistanceTo(ReducedCharacterState *other){
		//these are the settings for bip3Dv3...
		//the joints are: body_neck, lHip, rHip, lKnee, rKnee, neck_head
		RelevantJoint joints[] = {{0, 1.5, 1}, {1, 1.5, 0.1}, {2, 1.5, 0.1}, {4, 1, 0.05}, {5, 1, 0.05}, {3, 1.5, 0.05}};
		double result = 0;
		Quaternion qa, qb;
		Vector3d va, vb;

		//for the root orientation only consider the heading independent orientation
		qa = computeHeading(this->getOrientation()).getComplexConjugate() * this->getOrientation();
		qb = computeHeading(other->getOrientation()).getComplexConjugate() * other->getOrientation();

		va = this->getOrientation().getComplexConjugate().rotate(this->getVelocity());
		vb = other->getOrientation().getComplexConjugate().rotate(other->getVelocity());

		result += 3 * distanceBetweenOrientations(qa, qb);
		result += 3 * (va-vb).dotProductWith(va-vb);

		//and now penalize the difference in root angular velocities
		va = this->getOrientation().getComplexConjugate().rotate(this->getAngularVelocity());
		vb = other->getOrientation().getComplexConjugate().rotate(other->getAngularVelocity());
		result += 3 * (va-vb).dotProductWith(va-vb);

		//now go through all the joints that are relevant, and penalize the differences in the orientations and angular velocities
		for (uint i=0;i<sizeof(joints)/sizeof(joints[1]);i++){
			qa = this->getJointRelativeOrientation(joints[i].jIndex);
			qb = other->getJointRelativeOrientation(joints[i].jIndex);
			va = this->getJointRelativeAngVelocity(joints[i].jIndex);
			vb = other->getJointRelativeAngVelocity(joints[i].jIndex);
			result += joints[i].wQ * distanceBetweenOrientations(qa, qb);
			result += joints[i].wV * (va-vb).dotProductWith(va-vb);
		}

		return result;
	}



	/**
		this method can be used to compute the distance between two reduced character states that both belong to the bip3dv3 model.
	*/
	inline double bip3dv2_computeDistanceTo(ReducedCharacterState *other){
		//these are the settings for bip3Dv3...
		//the joints are: pelvis_torso, lHip, rHip, lKnee, rKnee
		RelevantJoint joints[] = {{0, 1.5, 1}, {1, 1.5, 0.5}, {2, 1.5, 0.5}, {6, 1, 0.2}, {7, 1, 0.2}};
		double result = 0;
		Quaternion qa, qb;
		Vector3d va, vb;

		qa = computeHeading(this->getOrientation()).getComplexConjugate() * this->getOrientation();
		qb = computeHeading(other->getOrientation()).getComplexConjugate() * other->getOrientation();

		va = this->getOrientation().getComplexConjugate().rotate(this->getVelocity());
		vb = other->getOrientation().getComplexConjugate().rotate(other->getVelocity());

		result += 3 * distanceBetweenOrientations(qa, qb);
		result += 3 * (va-vb).dotProductWith(va-vb);

		//and now penalize the difference in root angular velocities
		va = this->getOrientation().getComplexConjugate().rotate(this->getAngularVelocity());
		vb = other->getOrientation().getComplexConjugate().rotate(other->getAngularVelocity());
		result += 3 * 0.1 * (va-vb).dotProductWith(va-vb);

		//now go through all the joints that are relevant, and penalize the differences in the orientations and angular velocities
		for (uint i=0;i<sizeof(joints)/sizeof(joints[1]);i++){
			qa = this->getJointRelativeOrientation(joints[i].jIndex);
			qb = other->getJointRelativeOrientation(joints[i].jIndex);
			va = this->getJointRelativeAngVelocity(joints[i].jIndex);
			vb = other->getJointRelativeAngVelocity(joints[i].jIndex);
			result += joints[i].wQ * distanceBetweenOrientations(qa, qb);
			result += 0.1 * joints[i].wV * (va-vb).dotProductWith(va-vb);
		}

		return result;
	}

};
