score = int(input("Score: "))

# if score >= 90 and score <= 100:
#     print("Grade A")
# elif score >= 80 and score < 90:
#     print("Grade B")
# elif score >= 70 and score < 80:
#     print("Grade C")
# else:
#     print("Not Applicable")

"""
    Insted of asking for two questions score >= 80 and score < 90 and joining then by and operator python allows to write it simply like written normally in maths 80 <= score < 90
"""

# Conditions written by if elif ladder are mutually exclusive

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
else:
    print("Not Applicable")

"""
    As the if elif are not the individually asked questions we can further make the code a little more readable like (assuming the score will be lesser than 100)
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 70:
        print("Grade C")
    else:
        print("Not Applicable")

    we know if the score is greate than 90 than only the first condition will execute even though all the below conditions are technically correct
    and if the score is say greater than 80 and the first condition is not executed than we indirectly know that it it less than 90
        we are inplicilty applying two conditions and make the code more readable.

"""
