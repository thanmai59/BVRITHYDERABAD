

print "Enter the first number "
num1=gets.to_i

print "Enter the second number "
num2=gets.to_i

print  "Enter the third number "
num3=gets.to_i

if num1>=num2 and num1>=num3
      puts "num1= #{num1} is the greatest number"

elsif num2>=num1 and num2>=num3
      puts "num2= #{num2} is the greatest number"

else
      puts "num3= #{num3} is the  greatest number"
end