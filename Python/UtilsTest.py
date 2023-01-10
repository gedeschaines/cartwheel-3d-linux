import Utils
import sys

def testPrintFunc(text):

   if text is not None:
      sys.stdout.write("testPrintFunc:\n")
      sys.stdout.write(text)

print("Invoking Utils.test() before registering print function.")
Utils.test()

print("Registering print function {0}".format(testPrintFunc.__name__))
Utils.registerPrintFunction(testPrintFunc)

print("Invoking Utils.test() after registering print function.")
Utils.test()

Utils.registerPrintFunction(None)

