# Write a Ruby Script to accept a filename from the user print the extension of that.

#file="D:/Desktop/sl-lab/prog4.rb"

puts "Enter the path: "
file=gets.chomp

#file name
fbname=File.basename file
puts "File name: " +fbname

#base name
bname=File.basename file,".rb"
puts "Base name: " +bname

#file extension
fextn=File.extname file
puts "Extension:" +fextn

#path name
pathname=File.dirname file
puts "Path name: " +pathname

