# write a Ruby script to find the greatest of three numbers.

greatest=0
puts "Enter three numbers"
a=gets.chomp
b=gets.chomp
c=gets.chomp

if a>b and a>c
 greatest=a
elsif b>a and b>c
 greatest=b
elsif c>a and c>b
greatest=c
end

puts "greatest number is #{greatest}"