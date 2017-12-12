#############################

# Method to set the array
#
# @param data [Array] row data
def set_array(
    data:
  )
  ((data[1]-1)...data[2]).each do |index|
    @array[index] = data[3]
  end
end

# Method to ask the array
#
# @param data [Array] row data
def ask_array(
    data:
  )
  max_product, min_product = 1, 1
  ((data[1]-1)...data[2]).each do |index|
    max_product *= @array[index]
  end
  ((data[3]-1)...data[4]).each do |index|
    min_product *= @array[index]
  end
  return -1 unless max_product.modulo(min_product).zero?
  (max_product/min_product).modulo(data[5])
end

#############################


limit = gets.strip.to_i
@array  = gets.strip.split(' ').map(&:to_i)

query = gets.strip.to_i

query_arr = []

(0...query).each { |index| query_arr[index] = gets.strip.split(' ').map(&:to_i) }


query_arr.each do |data|
  if data[0] == 1
    set_array(data: data)
  else
    puts ask_array(data: data)
  end
end
