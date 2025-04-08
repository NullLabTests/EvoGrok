import re
import math

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
        else:
            document_type = 'unknown'
        
        # Extract and process the title of the HTML document
        title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
        title = title_match.group(1) if title_match else 'unknown title'
        
        # Calculate the length of the document
        document_length = len(input_data)
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted(['html document', document_type, title.lower(), f'{document_length} characters']))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it into words, sort them, and join with commas
        words = str(result).lower().split()
        
        # If the result is a number, add its square root and logarithm to the output
        if isinstance(result, (int, float)):
            words.append(str(round(result**0.5, 2)))
            words.append(str(round(math.log(abs(result) + 1), 2)))
        
        # Add the length of the result string
        words.append(f'{len(str(result))} characters')
        
        return ','.join(sorted(words))
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        words = str(input_data).lower().split()
        
        # Count the number of unique words and add it to the output
        unique_word_count = len(set(words))
        words.append(f'{unique_word_count} unique words')
        
        # Calculate the average word length
        total_length = sum(len(word) for word in words)
        avg_word_length = round(total_length / len(words), 2) if words else 0
        words.append(f'average word length: {avg_word_length}')
        
        # Add the total character count
        words.append(f'{len(input_data)} characters')
        
        return ','.join(sorted(words))