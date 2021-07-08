#comment
#file = "/Desktop/sl/prog3.rb"

puts "Enter file name"
file = gets.chomp

#file name
fbname = File.basename file
puts "file name: " +fbname
#base name
bname = File.basename file,".rb"
puts "Base name: " + bname

#file extention
fextn = File.extname file
puts "Extension:" +fextn

#path name
pathname = File.dirname file
puts "path name: "+pathname