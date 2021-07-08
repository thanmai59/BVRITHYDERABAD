def multiple_string(str,n)
    return str*n
end

print "Enter string :" "\n"
s = gets.chomp
print "Enter N value: " "\n"
n = gets.chomp.to_i

print multiple_string(s,n),  "\n"
