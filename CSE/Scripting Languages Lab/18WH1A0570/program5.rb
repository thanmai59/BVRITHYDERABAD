# Write a Ruby script to find the greatest of three numbers.

puts "Enter the 1st no: "
x = gets.to_i
puts "Enter the 2nd no: "
y = gets.to_i
puts "Enter the 3rd no: "
z = gets.to_i

if x >= y and x >= z
   puts "x = #{x} is the greatest number."
elsif y >= z and y >= x
   puts "y = #{y} is the greatest number."
else
   puts "z = #{z} is the greatest number."
end