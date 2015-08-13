# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

new_list = []

def nested_string(list1):
	for element in list1:
		if (type(element) == list):
			for elem in element:
				new_list.append(elem.capitalize())
		else:
			new_list.append(element.capitalize())
	print new_list			
		
	
def main():
	 #nested_string(['apple', ['bear','ll'], 'cat'])
	 pass
if __name__ == '__main__':
    main()