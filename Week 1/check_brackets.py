#python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
#foo(bar[i);

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    right = False
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i))
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack:
               left = opening_brackets_stack.pop().char
               if are_matching(left,next):
               	  pass
               elif are_matching(left,next) == False:
               	  mismatch = i+1
                  right = True
                  break   
            else: 
               right = True
               mismatch = i+1
               break
            pass
           
    if right:
       mismatch = mismatch
    elif not opening_brackets_stack:
       mismatch = "Success"
    else:
       mismatch = opening_brackets_stack.pop(0).position+1
    return mismatch
      

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
