puts "Enter the value of x: "
x = gets.to_i

puts "Enter the value of y: "
y = gets.to_i

puts "Enter the value of z: "
z = gets.to_i

if x >= y and x >= z
     puts "x = #{x} is greatest."
elsif y >= z and y >= x 
     puts "y = #{y} is greatest."
else 
     puts "z = #{z} is greatest."
end
