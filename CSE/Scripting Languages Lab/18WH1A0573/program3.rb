# Write a Ruby script which accept the user's first and last name and print them in reverse order with a space between them

puts "Enter first name: "
fname = gets.chomp
puts "Enter last name: "
lname = gets.chomp
puts "Before reversing: "
puts "#{fname} #{lname}"
puts "After reversing: "
puts "#{lname} #{fname}"