#######################

# Method to find the changed letters in sami's
# message to earth
#
# @param message [String] sami's message to earth
#
# @return [Number] Number of letters changed
def get_count_of_changed_letters(
    message:
)
  # Split the message into an array of 3 characters
  msg_array = message.split(/(\S{3})/).reject(&:empty?)
  # define default message
  default_msg = %w[S O S]
  letters_changed = 0
  msg_array.each do |msg|
    arr = msg.split('')
    arr.each_index { |index| letters_changed += 1 unless arr[index].eql?(default_msg[index]) }
  end
  letters_changed
end

#######################

message = gets.strip

puts get_count_of_changed_letters(message: message)
