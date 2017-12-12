
no_of_strings = gets.strip.to_i
string_arr = []

(0...no_of_strings).each { |index| string_arr[index] = gets.strip }

query = gets.strip.to_i
l, r, s = [], [] ,[]
(0...query).each do |index|
  l[index], r[index], s[index] = gets.strip.split(' ')
end

(0...query).each do |index|
  result = 0
  # Increment counter if the string is lexicographically smaller or eq
  string_arr[(l[index].to_i-1)..(r[index].to_i-1)].each { |string| result += 1 if string <= s[index] }
  puts result
end
