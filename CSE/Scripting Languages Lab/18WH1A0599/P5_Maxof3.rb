print "Enter 3 numbers "
n1 = gets.chomp.to_i
n2 = gets.chomp.to_i
n3 = gets.chomp.to_i

if n1 > n2 and n1 > n3
    puts "n1 = #{n1} is greatest of 3"
elsif n2>n3
    puts "n2 = #{n2} is greatest of 3"
elsif n3 > n1
    puts "n3 = #{n3} is greatest of 3"
else
    puts "error"

end
