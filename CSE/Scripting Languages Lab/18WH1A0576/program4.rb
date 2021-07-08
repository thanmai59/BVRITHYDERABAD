# Write a Ruby script to accept a filename from the user print the extension of that.

puts "Enter the file name"
file = gets.chomp

#file name
fbname=File.basename file
puts "File name: " +fbname

#base name
bname=File.basename file,".rb"
puts "Base name: " +bname

#file extension
fextn=File.extname file
puts "Extention:" +fextn

#path name
pathname=File.dirname file
puts "Path name: " +pathname