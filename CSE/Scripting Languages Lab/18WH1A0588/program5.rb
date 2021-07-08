#Write a Ruby script to find the greatest of three numbers

puts "Enter the value of a :"
a = gets.to_i
puts "Enter the value of b :"
b = gets.to_i
puts "Enter the value of c :"
c = gets.to_i

if a >= b and a >= c
   puts "a = #{a} is greatest."
elsif b >= c and b >= a
   puts "b = #{b} is greatest."
else 
   puts "c = #{c} is greatest."
end