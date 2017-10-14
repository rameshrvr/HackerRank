# Get the input
limit = gets.strip.to_i
array = []
# Scan the array
(0...limit).each { |index| array[index] = gets.strip.to_i }
# Sort the array
array.sort!

print array.join("\n")
