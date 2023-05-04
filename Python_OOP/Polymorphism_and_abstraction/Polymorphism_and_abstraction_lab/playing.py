def start_playing(object):
    return object.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"


children = Children()
guitar = Guitar()
print(start_playing(guitar))
print(start_playing(children))

