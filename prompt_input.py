def get_formatted_name(first_name, middle_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = first_name + ' ' + middle_name + ' ' + last_name
 return full_name.title()

print(get_formatted_name('john', 'lee', 'hooker'))
