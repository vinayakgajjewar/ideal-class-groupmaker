import reader
import sys
import brute_force

# Get class preferences
class_prefs = reader.get_class_prefs("")

print(sys.argv)
print(class_prefs)
print(brute_force.randomize(class_prefs))
