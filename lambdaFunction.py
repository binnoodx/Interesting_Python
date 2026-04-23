#<--------------Example 01--------------->

#Normal Function to calculate Sum
def sum(num1 , num2):
    return num1 + num2;
print("\nThe Sum of 2 and 7 using Normal Function is ", sum(2,7))

#Lambda Function to Calculate Sum
lamba_sum  = lambda num1 , num2 : num1+num2
print("\nThe Sum of 2 and 7 using lambda Function is ", lamba_sum(2,7))



#<--------------Example 02--------------->

#Normal Recursion Function to calculate factorial of 5
def fact(num):
    prod = 1
    if(num == 1):
        return 1;
    else:
        return num * fact(num-1);

print("\nThe Factorial of 5 using normal function is ", fact(5))


#Lambda Function to calculate Factorial of 5
lambda_fact = lambda num:1 if num == 1 or num == 0 else num*lambda_fact(num-1)
print("\nThe Factorial of 5 using lambda function is ", lambda_fact(5))


#Lambda function in map() and filter()

my_list = [1,3,5,6,8]


map_lambda = list(map(lambda num :num * num , my_list ))
# It makes list of those numbers of square of those which are mapped on original list
print("\nThe New list of squared number is" , map_lambda)

filter_lambda = list(filter(lambda num : num%2!=0 , my_list))
# It make new list filtering out those number which are odd only
print("\nThe New list of only odd numbers is " , filter_lambda)
print("\n")
