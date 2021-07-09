#greatest of 3 numbers

puts "Enter 3 numbers : "
a = gets.to_i
b = gets.to_i
c = gets.to_i
if a >= b && a >= c
   puts "#{a} is greater"
elsif b>= a && b >= c
   puts "#{b} is greater"
else
   puts "#{c} is greater"
end