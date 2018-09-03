from kazoo.client import KazooClient

class ArtemisClass(object):
    def __init__(self, args):
        zk = KazooClient(hosts='127.0.0.1:2181')
        zk.start()

        #zk.ensure_path("/artemis/locations")
        locations =  zk.get_children("/artemis/locations/")
        # In the end, stop it
        zk.stop()
        def check_location(location):
            if location not in locations: return False
            return True

        INVALID = False
        if (check_location(args.location) == False):
            INVALID = True
        else: self.location = args.location

