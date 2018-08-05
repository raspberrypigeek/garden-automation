class ArtemisClass(object):
    def __init__(self, args):
        def check_location(location):
            if location not in {"frontgarden", "backgarden"}: return False
            return True

        INVALID = False
        if (check_location(args.location) == False):
            INVALID = True
        else: self.location = args.location

