
#write a ruby script which accepts the user's first and last name and print them in reverse order with a space between them.

puts "Input your first name:"
fname = gets.chomp   #chomp method is used to remove newline from the string

puts "Input your last name:"
lname = gets.chomp

puts "Hello!,#{lname} #{fname}"