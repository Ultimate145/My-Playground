#Fizzbuzz
#if x is divisible by 2 (even) print fizz
#if x is divisible by 3 print buzz
#if x is not divisible by either number print an empty line

#example
#x=2
#fizz
#x=6
#fizzbuzz

fizz=3
buzz=5

for x in range (1,51):
    
    if x%(fizz*buzz)==0:
          print("fizzbuzz")
          
    elif x%fizz==0:
          print("fizz")
       
    elif x%buzz==0:
          print("buzz")

    else:
        print()
        

        
