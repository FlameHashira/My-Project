n_terms =int(input("How many terms the user wants to print?"))
#for first 2 terms
n_1=0
n_2=1
count=0
#Now, we will check if the given number us valid
if n_terms<=0:
    print("Please enter postive integer")
elif n_terms==1:
   print(" The Fibonacci swquence of the numbers uoto", num)
   print(n_1)
else:
    print("The fibonacci sequence of the numberis:")
    while count<n_terms:
        print(n_1)
        nth = n_1+n_2

        n_1=n_2
        n_2=nth
        count+=1
