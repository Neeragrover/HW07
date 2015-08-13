# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(list1):
	main_sum = 0
	for element in list1:
		if type(element) == int:
			main_sum = main_sum + element
		else:
			main_sum = main_sum + sum(element)
	return main_sum
		
	
def main():
	pass
		
if __name__ == '__main__':
    main()