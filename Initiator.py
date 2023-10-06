from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from MpTdSelector import cMpTdSelection
from ExampleWork import cExample
from Parameters import *

def main():
        # Create objects
        oExample = cExample()
        oMpTdSelector = cMpTdSelection()

        # Use the selector to call the function
        result1 = oMpTdSelector.mp_mt_selector('mt', oExample.factorial, [1250])
        print(result1)
        result2 = oMpTdSelector.mp_mt_selector('mp', oExample.factorial, [1250])
        print(result2)
        result3 = oMpTdSelector.mp_mt_selector('mp', oExample.factorial, [1250])
        print(result3)
        result4 = oMpTdSelector.mp_mt_selector('mp', oExample.factorial, [1250])
        print(result4)

if __name__ == '__main__':
    main()
