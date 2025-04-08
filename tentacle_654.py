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
        
        # Extract and count the number of unique classes in the HTML
        class_matches = re.findall(r'class="([^"]*)"', input_data, re.IGNORECASE)
        unique_classes = len(set(' '.join(class_matches).split()))
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted([
            'html document',
            document_type,
            title.lower(),
            f'{document_length} characters',
            f'{unique_classes} unique classes'
        ]))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it into words, sort them, and join with commas
        words = str(result).lower().split()
        
        # If the result is a number, add its square root, logarithm, and factorial to the output
        if isinstance(result, (int, float)):
            words.append(str(round(math.sqrt(result), 2)))
            words.append(str(round(math.log(result), 2)))
            words.append(str(math.factorial(int(result)) if result.is_integer() and result >= 0 else 'n/a'))
        
        # Add the type of the result to the output
        words.append(type(result).__name__)
        
        # Calculate and add the length of the result string
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
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        words.append(f'average word length: {round(avg_word_length, 2)}')
        
        # Count the number of digits in the input
        digit_count = sum(c.isdigit() for c in input_data)
        words.append(f'{digit_count} digits')
        
        return ','.join(sorted(words))