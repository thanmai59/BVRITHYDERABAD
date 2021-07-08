#x=gets.to_i
puts "enter three numbers"
x=gets.chomp
y=gets.chomp
z=gets.chomp
if x >= y and x >= z
     puts "x = #{x} is greatest."
elsif y >= z and y >= x 
     puts "y = #{y} is greatest."
else 
     puts "z = #{z} is greatest."
end

