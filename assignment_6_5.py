# Assignment 6.5
# Write code using find() and string slicing (see section 6.10) to extract the number
# at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

# -- given input
text = "X-DSPAM-Confidence:    0.8475"

# -- remove whitespaces
text = text.replace(" ", "")

# -- find index for ':' and string length
index = text.find(":")
length = len(text)

# -- slice
output = text[index+1:length]
output = float(output)
print(output)