# Write a Ruby Script to find the greatest of three numbers.

puts "Enter 3 numbers: "
#puts "Enter num1: "
num1 = gets.chomp

#puts "Enter num2: "
num2 = gets.chomp

#puts "Enter num3: "
num3 = gets.chomp

if num1>num2
   if num1>num3
      puts "num1 is greater"
   else
      puts "num3 is greater"
   end
elseif num2>num3
     puts "num2 is greater"
else
     puts "num3 is greater"
end 