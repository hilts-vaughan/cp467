__author__ = 'Brandon'

import filter_test
import trainer_main
import Comparison_main
import sys
import platform


print("CP467 - Image Processing: Mean Norm Clustering\n")
# Pre-amble; good for debugging information
print("Operating System: " + platform.version())
print("Python: " + sys.version + "\n")

while True:

    print("What would you like to do?")

    print("1) Run filters")
    print("2) Run training algorithm")
    print("3) Run comparison")
    print("4) Exit\n")

    user_selection = input("Enter a choice: ")
    if user_selection is "1":
        filter_test.filter_test()

    elif user_selection is "2":
        trainer_main.trainer_main()

    elif user_selection is "3":
        Comparison_main.comparison_main()
    elif user_selection is '4':
        exit()
    else:
        print("Enter a valid option.")
