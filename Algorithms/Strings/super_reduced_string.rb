# Get the input
string_array = gets.strip.split('')

# Set index to zero
index = 0

until (index == string_array.length) do
  # If a pair found delete them and start the search from begining	
  if string_array[index].eql? string_array[index+1]
    2.times { string_array.delete_at(index) }
    index = 0
    next
  end
  index += 1
end

if index.zero?
  print 'Empty String'
else
  print string_array.join('')
end
