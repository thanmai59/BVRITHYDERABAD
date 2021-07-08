#greatest of three numbers
puts "Enter the 3 numbers which you want to compare:"
puts " a :"
a = gets.chomp
puts " b :"
b = gets.chomp
puts " c:"
c = gets.chomp
if ( a>b)
    if(a>c)
        print "a is the greatest amoung three"
    else
        print "c is the greatest amoung three"
    end
else
   if(b>c)
       print "b is the greatest amoung three"
    else
        print "c is the greatest amoung three"
    end
end
      