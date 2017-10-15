########################

# Method to rate alice and bob
#
# @param alice [Array]
# @param bob [Array]
#
# @return [Array] alice_comp, bob_comp
def rate_alice_and_bob(
    alice:,
    bob:
  )
  alice_comp, bob_comp = 0, 0
  alice.each_index do |index|
    if alice[index] > bob[index]
      alice_comp += 1
    elsif alice[index] < bob[index]
      bob_comp += 1
    end
  end
  [alice_comp, bob_comp]
end

########################

alice = gets.split(' ').map(&:to_i)
bob = gets.split(' ').map(&:to_i)

result = rate_alice_and_bob(alice: alice, bob: bob)

print "#{result[0]} #{result[1]}"
