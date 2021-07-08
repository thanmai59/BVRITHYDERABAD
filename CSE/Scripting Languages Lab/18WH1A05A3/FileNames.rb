# write a ruby script to accept a file name from the user, print the extension of that.

puts " Enter the path of the file:"
file = gets.chomp
#file name
fbname = File.basename file
puts "File Name : " +fbname

#base name
bname = File.basename file,".rb"
puts "Base Name : " +bname

#file extention
fextn = File.extname file
puts "extention:" + fextn

#path name
pathname = File.dirname file
puts "path name: " + pathname