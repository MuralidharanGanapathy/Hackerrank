import re
def count_substring(string, sub_string):
    return len(re.findall("(?={})".format(sub_string), string))

