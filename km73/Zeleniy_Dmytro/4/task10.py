start_row  = int(input("Enter start row: "))
start_column  = int(input("Enter start column: "))

finish_row = int(input("Enter finish row: "))
finish_column = int(input("Enter finish column: "))

if (start_row > 0 and start_row <= 8 
    and start_column > 0 and start_column <= 8
    and finish_row > 0 and finish_row <= 8 
    and finish_column > 0 and finish_column <= 8):
    
    if (abs(start_row - start_column) == abs(finish_row - finish_column) 
        or (start_column + start_row) == (finish_column + finish_row)
        or start_row == finish_row
        or start_column == finish_column):
        answer = "Yes"
    else:
        answer = "No"

else:
    answer = "NOT CORRET DATA!"

print(answer)