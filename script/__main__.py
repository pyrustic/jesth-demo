import os.path
import pprint
from jesth import read


filename = "jesthfile"

# check filename existence
if not os.path.exists(filename):
    raise Exception("No jesthfile in the current working directory")

# read the jesthfile
document = read(filename)

# convert the top anonymous section into a dict
header = ""  # anonymous section
section = document.get(header)  # by default, sub_index is 0 (more below)
dict_data = section.to_dict(strict=False)  # arg set to preserve comments

# print the body of the section
print("\nTHIS IS THE BODY OF THE SECTION")
print("===============================\n")
pprint.pprint(section.body)

print("\n\n\n")

# pretty print the dict data
print("THIS IS THE BODY AS CONVERTED INTO A DICTIONARY")
print("===============================================\n")
pprint.pprint(dict_data)



# NOTE: the get method of the document object accept the sub_index argument
# to specify what section to return when many sections share the same
# header. By default, for pragmatic reasons, index is set to 0.
# Therefore when a section is the only one to have a given header,
# it will still be returned. And in the case of multiple sections
# sharing same header, the first of them will be returned.
