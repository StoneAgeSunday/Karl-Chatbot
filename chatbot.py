from responder import *

comment = ''
while comment != 'Goodbye':
    comment = input('User: ')
    response = getResponse(comment)
    print("Karl: " + response)
