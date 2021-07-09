#write a ruby script to accept a filename from the user print the extension of that.

puts "Enter file name"
file=gets.chomp

#file name
fname=File.basename file
puts "File name:"+fname

#base name
bname=File.basename file,".rb"
puts "Base name:"+bname

#file extension
fextn=File.extname file
puts "Extension:"+fextn

#path name
pathname=File.dirname file
puts "Path name:"+pathname