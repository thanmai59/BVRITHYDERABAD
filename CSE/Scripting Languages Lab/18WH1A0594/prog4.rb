puts "Enter file name:"
file = gets.chomp
fbname = File.basename file
puts "File name : " + fbname

bname = File.basename file, ".rb"
puts "Base name : " + bname

extension = File.extname file
puts "Extension : " + extension

path = File.dirname file
puts "Path name : " + path
