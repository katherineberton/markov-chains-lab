"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    #use .read() function to turn contents of the file into a single list
    contents = open(file_path).read()
    
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    #               create the list with elements single words from the file being imported

    #rstrip the file's text and replace line breaks with spaces for later use of the .split(" ") function
    formatted = text_string.rstrip().replace("\n", " ")
    
    #then use .split(" ") to turn it into a list
    list_of_words = formatted.split(" ")
    

    #                populate the dictionary

    #for loop over a range of the list to create dict keys, range to accommodate the final tuple which starts at index len(list_of_words) - 2
    for i in range(0,(len(list_of_words)-1)):

        #create variable named tup equal to (word at index i, following word)
        tup = (list_of_words[i], list_of_words[i+1])

        #if the resultant tup is the last possible tuple in the list:
        if i == len(list_of_words) - 2:

            #assign the value to a list containing empty string
            chains[tup] = [""]

        #otherwise, if it's any other tuple than the last one
        else:

            #if the tuple is already a key in the dictionary:
            if tup in chains:

                #append the value list with the word following the tuple
                chains[tup].append(list_of_words[i+2])

            #otherwise, if it's not already in the list
            else:

                #create new key value pair with key the tuple and value a list containing only one element: the word following the tuple in the list
                chains[tup] = [list_of_words[i+2]]
    

    return chains


def make_text(chains):
    """Return text from chains."""

    #blank list to receive the words from the list
    words = []

    #starts with a random choice of the keys in dictionary chains being passed in
    initial_key = choice(list(chains))

    words.append(initial_key[0]) #add first thing in the retrieved key to words list
    words.append(initial_key[1]) #add second thing in the retrieved key to words list

    #declare current_key variable for use in the loop
    current_key = initial_key

    #leave the loop when we have reached the end of the text, or in other words, when the value of the tuple is ""
    while chains[current_key] != [""]:

        #choose random value from chains at current key    
        new_value = choice(chains[current_key])

        #appends words list with the retrieved value
        words.append(new_value)

        #updates current_key to drop first item and add the previously retrieved value
        current_key = (current_key[1], new_value)

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
