alice = gets.split(' ').map(&:to_i)
bob = gets.split(' ').map(&:to_i)
alice_comp, bob_comp = 0, 0
(0..alice.length-1).each do |count|
    if alice[count] > bob[count]
        alice_comp += 1
    elsif alice[count] < bob[count]
        bob_comp += 1
    else
    	alice_comp += 1
        bob_comp += 1
    end
end
print "#{alice_comp} #{bob_comp}"