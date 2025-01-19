programme_dictionary={
    "Key1": "Value1" ,
    "Key2": "Value2" ,
    "Key3": "Value3"
}
print (programme_dictionary)
print (programme_dictionary["Key1"]) ##Show key1 only

##Adding new Dictionary
programme_dictionary["Key4"] = "Key4" ##Added the Key4

print(programme_dictionary)

##Create Empty dictionary
empty_dictionary = {}
print (empty_dictionary)

##Edit the item in dictionary
programme_dictionary["Key4"] = "This was added by code"
print (programme_dictionary)

##Loop Through Dictionary
for thing in programme_dictionary:
    print (thing)
    print (programme_dictionary[thing])

