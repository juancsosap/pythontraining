# The text could be modifed using the % operator
# This method is supported but was replaced, then it is not recommended
text = "My name is %s %s and I'm %d years old"
formated_text = text % ("Juan", "Sosa", 36)
print(formated_text, end="\n\n")

# The new way to format the text is using the format method
text = "My name is {} {} and I'm {} years old"
formated_text = text.format("Juan", "Sosa", 36)
print(formated_text, end="\n\n")

# IDs from 0 could be assigned to each item to don't repeat values
text = "My name is {0} {1} and My email is {0}.{1}@company.com"
formated_text = text.format("Juan", "Sosa")
print(formated_text, end="\n\n")

# Intead of index numbers to identificate each element, could be user a name
template = "({id}) {name} {surname}\n"
print(template.format(id = 123, name = "Juan", surname = "Sosa"))

# The format options are included after the (:) symbol
# Could be defined the minimum size required for the text
# The remaining characters will be fill with spaces (default)
template = "| {0:10} | {1:10} |"
print(template.format("NAME", "SURNAME"))
print(template.format("----------", "----------"))
print(template.format("Juan", "Sosa"))
print(template.format("Carlos", "Peña"))
print(template.format("----------", "----------"), end="\n\n")

# Longer texts could occupate more space
# Could be truncated if it is longer than the defined size {:MIN.MAX}
template = "| {0:10} | {1:10} |"
print(template.format("NAME", "SURNAME"))
print(template.format("----------", "----------"))
print(template.format("Nabucodonozor", "Gutierrez"))
template = "| {0:10.10} | {1:10.10} |"
print(template.format("Nabucodonozor", "Gutierrez"))
print(template.format("----------", "----------"), end="\n\n")

# The remaining characters could be fill with another characters
template = "({id:08}) {name:10} {surname:10}\n"
print(template.format(id = 123, name = "Juan", surname = "Sosa"))

# The text could be aligned to the left (<), right (>) or center (^)
template = " {id:<8} {name:^10} {surname:^10} {age:>5}"
print(template.format(id = "ID", name = "NAME", surname = "SURNAME", age = "AGE"))
template = "{:-<38}"
print(template.format(""))
template = " {id:<08} {name:^10} {surname:^10} {age:>5}"
print(template.format(id = 123, name = "Juan", surname = "Sosa", age = 36))
print(template.format(id = 456, name = "Carlos", surname = "Peña", age = 35))
template = "{:-<38}\n"
print(template.format(""))

# Number could be formated properlly according to the type
# For integer numbers could be included the thousand separator and the leading zeros
template = " {id:08d} - {name} {surname} : {days:,d} days\n"
print(template.format(id = 123, name = "Juan", surname = "Sosa", days = 1325))
# For float numbers could be included the thousand separator, the leading zeros and
# the amount of decimals
template = " {id:08d} - {name} {surname} : {salary:,.2f} CLP\n"
print(template.format(id = 123, name = "Juan", surname = "Sosa", salary = 2507427.1277))

# Another format rules could be aplied for diferent types of objects
