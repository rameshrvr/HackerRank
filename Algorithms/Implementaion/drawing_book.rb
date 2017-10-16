##########################

# Method to calculate minimum number of
# page turns
#
# @param pages [Number] No of pages in the book
# @param page_no [Number] page number where we gonna land
#
# @return [Number] Minimum no of turns
def calc_minimum_page_turn(
    pages:,
    page_no:
  )
  if page_no == pages-1 && pages.odd?
    # If no_of_pages is odd and the page we want to land is next to it?
    # then return 0
    return 0
  elsif page_no <= pages/2
    # If result page is before the middle of the book then return page / 2
    return page_no/2
  else
    # If result page is after the middle then return (total pages / 2) - (result page / 2)
    return (pages/2) - (page_no/2)
  end
end

##########################

total_no_pages = gets.strip.to_i
page_to_turn = gets.strip.to_i

# Print result
puts calc_minimum_page_turn(pages: total_no_pages, page_no: page_to_turn)
