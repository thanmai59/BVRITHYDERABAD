# file="/Users/User/Desktop/printExtension.rb"
puts "Input your file name:"
file=gets.chomp

#File name
fbname=File.basename file
puts "File name : " +fbname

#Base name
bname=File.basename file,".rb"
puts "Base name: " +bname

#file extension
fextn=File.extname file
puts "Extension:" +fextn

#path name 
pathname=File.dirname file
puts "Path name: " +pathname