puts "Enter num 1"
x = gets.chomp.to_i

puts "Enter num 2"
y = gets.chomp.to_i

puts "Enter num 3"
z = gets.chomp.to_i

if x >= y and x >= z
     puts "#{x} is greatest."
elsif y >= z and y >= x 
     puts "#{y} is greatest."
else 
     puts "#{z} is greatest."
end


