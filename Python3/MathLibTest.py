import Utils
import MathLib
import sys

def printFunc(text):
    if text is not None:
        sys.stdout.write(text)
    
print("Using Vector3d._print() method.\n")

x = MathLib.Vector3d()
x.setValues(10,0.44,-132)
print("x = ", end=" ")
x._print()

y = MathLib.Vector3d()
y.setValues(3,11,2)
print("y = ", end=" ")
y._print()

x.addScaledVector(y,0.5)
print("x + 0.5y = ", end=" ")
x._print()

print("\nRegistering print function: {0}\n".format(printFunc.__name__))

Utils.registerPrintFunction(printFunc)

print("Using Vector3d.printTuple() method.\n")

x = MathLib.Vector3d()
x.setValues(10,0.44,-132)
print("x = ", end=" ")
x.printTuple()

y = MathLib.Vector3d()
y.setValues(3,11,2)
print("y = ", end=" ")
y.printTuple()

x.addScaledVector(y,0.5)
print("x + 0.5y = ", end=" ")
x.printTuple()

print("\nChecking Vector3d element indexing:\n")

print("x.x =%lf, x.y =%lf, x.z =%lf " % (x.x, x.y, x.z) )
print("x[0]=%lf, x[1]=%lf, x[2]=%lf " % (x[0], x[1], x[2]) )

Utils.registerPrintFunction(None)
