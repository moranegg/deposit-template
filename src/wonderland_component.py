# Copyright (C) 2015-2019  The wonderland team
# License: GNU General Public License version 3, or any later version


import json


class WonderlandCrawler():


    def __init__(self):


    def find_wonderland(self, entry_pattern):


class WonderlandDoor():

    def __init__(self):
        pass

    def compute_door(context, raw_key):
        """Retrieve entry to Wonderland
        """
        try:
            # the existing map to wonderland
            current_map = wonderland_mapping.get(context)
            # generates map in readable format
            map_format = read(context, raw_key)
            result = {}
            for step in map:
                value = step.get(map.get(location))
                result[location] = value
            return result
        except Exception:
            return None

        def parse_from_xml():
            """
            Not sure need a specific parse from xml
            """
            pass

        def parse_txt_to_dict():
            pass



def main():
    print "Hello Wonderland!"


if __name__ == '__main__':
    main()
