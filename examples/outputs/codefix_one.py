

main_string = "pysharper will fix this don't worry!"

check_strings = ("pysharper will fix this don't worry!", 'hello world, this is the first code smell', 'it will fix this error by changing this datatype', 'it will change this to a tuple', 'this is because nothing is being added/removed/edited from the datatype', 'therefore python is using up more ram than is needed with the extra head-space!')


print(main_string in check_strings)  # Should return True before & after the refactor
