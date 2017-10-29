#############################

# Method to return count of lexicographically smaller
# or equalent string
#
# @param string_array [Array] array containing all possible strings
# @param l [Number] start index
# @param r [Number] end index
# @param s [String] string to compare with
def count_lex_smaller_string(
    string_array:, l:, r:, s:
  )
  result = 0
  # Increment counter if the string is lexicographically smaller or eq
  string_array[(l-1)..(r-1)].each { |string| result += 1 if string <= s }
  result
end

#############################

no_of_strings = gets.strip.to_i
string_arr = []

(0...no_of_strings).each { |index| string_arr[index] = gets.strip }

query = gets.strip.to_i
l, r, s = [], [] ,[]
(0...query).each do |index|
  l[index], r[index], s[index] = gets.strip.split(' ')
end

(0...query).each do |index|
  puts count_lex_smaller_string(
    string_array: string_arr,
    l: l[index].to_i,
    r: r[index].to_i,
    s: s[index]
  )
end
