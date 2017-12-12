######################

# Method to perform the cut operation in all sticks
# and print the operation performed
#
# @param stick_array [Array] Array of stick length
#
# @return none (It will just print the number of operation performed)
def cut_the_sticks(
    stick_array:
)
  # Perform the below operations until the array gets empty
  until stick_array.empty?
    # Print the no of stick for which the cut will be done
    puts stick_array.length
    # Get the minimum value from the array
    min_value = stick_array.min
    # Perform cut operation
    stick_array.map! { |stick| stick - min_value }
    # Remove 0s from the array
    stick_array.delete(0)
  end
end

######################

_limit = gets.strip.to_i
stick_array = gets.strip.split(' ').map(&:to_i)

cut_the_sticks(stick_array: stick_array)
