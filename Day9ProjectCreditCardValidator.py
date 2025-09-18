# 5893804115457289

card_number = list(input("Enter a card number : ").strip())

checked_digit = card_number.pop()

card_number.reverse()



index = 0 

processed_number = []

for index , digit in enumerate(card_number) :
    if index % 2 == 0 :
        double_digit = int(digit) * 2

        if double_digit > 9 :
            double_digit = double_digit - 9
          
        
        processed_number.append(double_digit)
        
    else :
         processed_number.append(int(digit))
    




final_check = sum(processed_number) + int(checked_digit)

if final_check % 10 == 0 :
    print("Valid Card Number !")
else :
    print("InValid Card Number !") 

