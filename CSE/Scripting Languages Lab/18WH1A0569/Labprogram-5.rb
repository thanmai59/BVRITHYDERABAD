puts "Take three numbers a,b,c-"
puts "Enter value of a : "
a = gets.chomp.to_i
puts "Enter value of b : "
b = gets.chomp.to_i
puts "Enter value of c : "
c = gets.chomp.to_i
if(a>=b and a>=c)
	puts "a = #{a} is greatest"
elsif(b>=c and b>=a)
	puts "b = #{b} is greatest"
else
	puts "c = #{c} is greatest"
end