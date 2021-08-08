print("Fizz Buzz Program")
print("There are bunch of kids sitting in a circle. They will speak numbers starting from 1")
print("first kid will say 1, second will say 2 but thrid kid will say Fizz as 3 is divisible by 3")
print("each kid which is getting a number divisible by 3 will say Fizz")
print("similarly each kid will say buzz if his/her number is divisible by 5")
print("similarly is a kid gets a numver that is divisible by 3 and 5 both e.g. 15 then he/she will dsay FizzBuzz")
print("Lets assume there are 100 kids and see how many Fizz, Buzz and FizzBuzz are there.")
fizz = 0
buzz = 0
fizzbuzz = 0
for number in range(1,101):
    if number%3==0 and number%5 == 0:
        fizzbuzz += 1
        print("fizzbuzz")
    elif number%3==0:
        fizz += 1
        print("fizz")
    elif number%5==0:
        buzz += 1
        print("buzz")
    else:
        print(number)
print(f"Total fizz are {fizz}, total buzz are {buzz} and total fizzbuzz are {fizzbuzz}")