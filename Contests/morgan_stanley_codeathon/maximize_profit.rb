################

# Method to calculate the maximum currency rate
#
# @param bitcoin: [Number] No of bitcoin ron has
# @param conversion_rate: [Array] conversion rate of bitcoin
# @param units: [Array] No of units ron can buy
# @param max_value: [Number] max value of currency
def calc_max_doller_value(
    bitcoin:,
    conversion_rate:,
    units:,
    max_value:
  )
  conversion_rate.each_with_index do |value, index|
    if bitcoin * value * units[index] > max_value
      max_value = bitcoin * value * units[index]
    end
  end
  max_value
end
################

n, m, k = gets.strip.split(' ').map(&:to_i)
conversion_rate = gets.strip.split(' ').map(&:to_i)
units = gets.strip.split(' ').map(&:to_i)

# Calculate the doller w.r.t bitcoin
max_value = m * k

# Print the result
puts calc_max_doller_value(
  bitcoin: m,
  conversion_rate: conversion_rate,
  units: units,
  max_value: max_value
)
