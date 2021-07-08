# write a ruby script to find the greatest of three numbers

puts "Enter the three numbers: "
num1,num2,num3 = gets.split.map(&:to_i)
#num2 = gets.chomp.to_i
#num3 = gets.chomp.to_i

if num1 > num2 and num1 > num3
	puts "#{num1} is larger than #{num2} and #{num3}"
elsif num2 > num3 and num2 > num1
	puts "#{num2} is larger than #{num1} and #{num3}"
else
	puts "#{num3} is larger than #{num1} and #{num2}"
end
