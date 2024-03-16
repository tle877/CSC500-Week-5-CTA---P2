book_nums = int(input("please input the the number of books you have purchased this month: "))
award = 0
if (book_nums == 2):
    award = 5
elif (book_nums == 4):
    award = 15
elif (book_nums == 6):
    award = 30   
elif (book_nums >=8):
    award = 60 

print("You earned : " + str(award) + " points")