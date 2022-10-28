
languages = [['English', 'Russian'], ['English'], ['English', 'German'], ['Chinese', 'Japanese']]
person4_language2 = languages[3][1]
print (person4_language2)
languages_copy = [person[:] for person in languages] # [['English', 'Russian'], ['English'], ['English', 'German'], ['Chinese', 'Japanese']]
print (languages_copy)

i = 0
for person in languages:
    i += 1
    for language in person:
        print("Сотрудник #" + str(i) + " знает " + language)


