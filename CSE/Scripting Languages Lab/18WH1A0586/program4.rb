# write a ruby script to accept a filename from the user print the extension of that

#file = "H:/3-2 subjects/SL Lab/program3.rb"    #here we are explicitly taking the file name


#Reading filename
puts "Enter the file name: "
file = gets.chomp

#filename
fname = File.basename file
puts "File name: " + fname

#basename

bname = File.basename file,".rb"   #to print file name without it's extension we have included .rb
puts "Base name : " + bname

#file extension

fextn = File.extname file
puts "Entension: "+ fextn

#path of the file

fpath = File.dirname file
puts "File path is: "+ fpath