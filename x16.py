word = raw_input('Dame una palabra ')

def is_palindrome(word):
	new_lst = [x for x in word]
	new_lst.reverse()
	back = ''.join(new_lst)

	if word == back:
		print 'It is palindrome'
	else:
		print 'It is not palindrome'

is_palindrome(word)

