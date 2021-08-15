# Python program to display the Fibonacci sequence

def recur_fibo(n):

    if n <= 1:
        return 1
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    
    # check if the number of terms is valid

nterms = 10
    
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
    
    

