counter = 0

def inception():
    global counter
    if (counter > 3):
        return 'done'

    counter += 1
    return inception()

print(inception())