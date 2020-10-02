#  Hint:  You may not need all of these.  Remove the unused functions.

#INPUT: Ticket(key, value) where key = "STARTING POINT" and value = "DESTINATION POINT"
#OUTPUT: 'route' which is a hash table containing the keys in order of the flight route. 
# In order means I will need a data type that keeps data in order, list or dictionary.
# Source location is the KEY, destination location is the VALUE. 
# Will start with NONE as the first key. 
# The first value will match the next sets' key, that set's value will match the next set's key.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    #given tickets (array of key,value pairs) and length (limit)
    #make hash table 'route' with 'length' slots all initialized to None
    route = [None] * length

    #keep a cache of the airport_codes
    airport_codes = {}

    #hashed keys become the start location and the values stored at each key are the destinations
    for ticket in tickets:
        airport_codes[ticket.source] = ticket.destination

    #no matter what input is given, the first key is going to be NONE, which with be assigned to the next pair's value DESTINATION, so initialize the first airport code as None
    start_airport_code = airport_codes["NONE"] #the first key in the cache of airport_codes

    #for each key in the range of the cache, the index will start at the start_airport_code (none) then will be re-assigned to the value of the next element's value, the loop will run and keep re-assigning the source to the destination
    for key in range(length):
        route[key] = start_airport_code

        start_airport_code = airport_codes[start_airport_code]

    return route

def test_short_case(self):
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")
    tickets = [ticket_1, ticket_2, ticket_3]
    result = reconstruct_trip(tickets, 3)

    return result

def test_another_case(self):
    ticket_1 = Ticket("NONE", "LAX")
    ticket_2 = Ticket("LAX", "TUL")
    ticket_3 = Ticket("TUL", "JFK")
    ticket_4 = Ticket("JFK", "NONE")
    tickets = [ticket_1, ticket_2, ticket_3, ticket_4]
    result = reconstruct_trip(tickets, 4)

    return result

print(test_short_case(""))
print(test_another_case(""))
