import Utils
import Physics

import sys

def _printFunc(text):

    if text is not None:
        sys.stdout.write(text)


# Register testPrinfFunc()
Utils.registerPrintFunction(_printFunc)

Physics.test()

Utils.registerPrintFunction(None)

