__author__ = 'Brandon'

import filter_test
import trainer_main
import Comparison_main
print("what would you like to do")
print("1) run filters")
print("2) run training algorithm")
print("3) run comparison")
while True:
    user_selection=input("please enter a number here")
    if user_selection=="1":
        filter_test.filter_test()

    elif user_selection=="2":
        trainer_main.trainer_main()

    elif user_selection=="3":
        Comparison_main.comparison_main()
    else:
        print("enter a 1 2 or 3")
