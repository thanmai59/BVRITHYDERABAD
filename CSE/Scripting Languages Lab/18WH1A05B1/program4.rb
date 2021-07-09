puts "Enter File Name"

file = gets.chomp

fbname=File.basename file

puts "File name: " +fbname

bname=File.basename file,".rb"

puts "Base name: " +bname

fextn=File.extname file

puts "Extension:" +fextn

fextn=File.extname file

puts "Extension:" +fextn