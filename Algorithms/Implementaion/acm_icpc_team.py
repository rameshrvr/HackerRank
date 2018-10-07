

def calc_max_no_of_topics(details, attendees):
    """
    Method to calculate max number of topics known
    by any two people in the ACM ICPC final

    Args:
            details: Details Array
            attendees: attendees count
    Return:
            None
    """
    result_array = []
    for index1 in xrange(0, attendees - 1):
        for index2 in xrange(index1, attendees):
            topics_combined = '{0:b}'.format(
                details[index1] | details[index2]
            )
            result_array.append(topics_combined.count('1'))
    max_topics_known = max(result_array)
    print max_topics_known
    print result_array.count(max_topics_known)
    return


############
temp = map(int, raw_input().rstrip().split())
attendees = temp[0]
no_of_topics = temp[1]
details = []
for _ in xrange(0, attendees):
    details.append(int(raw_input().rstrip(), 2))

calc_max_no_of_topics(details, attendees)
############
