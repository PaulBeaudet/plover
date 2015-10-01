# Copyright (c) 2013 Hesky Fisher
# See LICENSE.txt for details.

import json
import unittest

DICT_PATH='plover/assets/dict.json'

DICT_PATH_MAIN='plover/assets/main.json'
DICT_PATH_COMMANDS='plover/assets/commands.json'

def read_key_pairs(pairs):
    d = {}
    for key, value in pairs:
        holder = []
        if key in d:
            holder = d[key]
        else:
            d[key] = holder
        holder.append(value)
    return d

class TestCase(unittest.TestCase):
    
    def test_no_duplicates_unsorted_file(self):
            
        d = json.load(open(DICT_PATH), object_pairs_hook=read_key_pairs)
        
        msg_list = []
        has_duplicate = False
        for key, value_list in d.items():
            if len(value_list) > 1:
                has_duplicate = True
                msg_list.append('key: %s\n' % key)
                for value in value_list:
                    msg_list.append('%s\n' % value)
        msg = ''.join(msg_list)
        self.assertFalse(has_duplicate, msg)

    def test_no_duplicates_categorized_files(self):

        d = json.load(open(DICT_PATH_MAIN), object_pairs_hook=read_key_pairs)
        d.update(json.load(open(DICT_PATH_COMMANDS), object_pairs_hook=read_key_pairs))

        msg_list = []
        has_duplicate = False
        for key, value_list in d.items():
            if len(value_list) > 1:
                has_duplicate = True
                msg_list.append('key: %s\n' % key)
                for value in value_list:
                    msg_list.append('%s\n' % value)
        msg = ''.join(msg_list)
        self.assertFalse(has_duplicate, msg)
