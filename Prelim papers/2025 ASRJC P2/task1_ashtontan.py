#Task 1.1
def encode_str(text, token):
    if text.isalpha() == False:
        return 'Text should only contain letters'
    
    if token in text:
        return 'Text should not contain token'
    
    count = 0 
    encoded_text = []
    while count < len(text):
        current = tet