#Write a ruby script to accept a filename from the user and print the extension of it.

#file = "/Users/srijan/Desktop/RUBY - SCRIPTING LANGUAGES/program4.rb"
puts "Enter File Name : "
file = gets.chomp

#filename
fbname = File.basename file
puts "File Name: " +fbname

#base name
bname = File.basename file,".rb"
puts "Base Name: "+bname

#file extension
fextn = File.extname file
puts "Extension: "+ fextn 

#path name
pathname = File.dirname file
puts "Path name: "+pathname

