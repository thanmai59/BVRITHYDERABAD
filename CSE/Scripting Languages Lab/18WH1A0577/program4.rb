puts "Enter the path of the file: "
file = gets.chomp

#file name
fbname = File.basename file
puts "File name: " + fbname

#base name
bname = File.basename file,".rb"
puts "Base name: " + bname

#file extention
fextn = File.extname file
puts "Extention: " + fextn

#path name
pathname = File.dirname file
puts "Path name: " + pathname