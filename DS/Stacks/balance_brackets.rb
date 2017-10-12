# Get the input from command line
query = gets.strip.to_i
bracket_array = []
query.times { bracket_array.push(gets.strip) }
# Defining the openeing and closing brakets
@closing_brac = ['}', ')', ']']
@pair_brac = ['()', '[]', '{}']

# Method to process the brackets and produce the result
def process_brackets(set:)
  result = 'YES'
  # Split the word into array
  array = set.split('')
  new_array = []
  # execute until the array gets empty
  until array.empty?
    # push the shifted array element until we found a closing bracket
    new_array.push(array.shift) until @closing_brac.include? array[0]
    # break the loop if we found a closing at the begining
    if new_array.empty?
      result = 'NO'
      break
    end
    temp = new_array.pop + array.shift
    # Break the loop if the pairs were not matching
    unless @pair_brac.include?(temp)
      result = 'NO'
      break
    end
  end
  result
end

# print the result
bracket_array.each { |array| puts process_brackets(set: array) }
