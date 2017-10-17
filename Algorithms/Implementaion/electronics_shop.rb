######################

# Method to calculate max amount that she spend on electronics
#
# @param [Array] Array of keyboad prize range
# @param [Array] Array of mouse prize range
# @param [Number] Maximum amount she has in her hand
#
# @return [Number] Maximun amount spend or -1
def cal_max_amount_spend(
    keyboard_prize:,
    mouse_prize:,
    amount:
)
  amount_spend = -1
  keyboard_prize.each do |k_prize|
    mouse_prize.each do |m_prize|
      sum = k_prize + m_prize
      # amout_spend should be sum if sum <= amount in her hand
      amount_spend = sum if sum <= amount && sum > amount_spend
    end
  end
  # Return the max amount that she spend
  amount_spend
end
######################

total_amount, _k_brands, _m_brands = gets.strip.split(' ').map(&:to_i)
keyboard_prize = gets.strip.split(' ').map(&:to_i)
mouse_prize = gets.strip.split(' ').map(&:to_i)

puts cal_max_amount_spend(
  keyboard_prize: keyboard_prize,
  mouse_prize: mouse_prize,
  amount: total_amount
)
