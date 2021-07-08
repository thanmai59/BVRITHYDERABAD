#file = "/home/dell/3-2 year/ScriptingLanguage/Ex1.rb"
print "Enter filename" "\n"
file = gets.chomp
fbname = File.basename file
puts "File name :" + fbname


bname = File.basename file, ".rb"
puts "Basename : " + bname

extname = File.extname(file)
puts "Extension : " + extname

