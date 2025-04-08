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
        
        # Count the number of tags in the document
        tag_count = len(re.findall(r'</?[a-zA-Z][^>]*>', input_data))
        
        # Calculate the average length of tag attributes
        attributes = re.findall(r'\s([a-zA-Z]+)=["\'].*?["\']', input_data)
        avg_attr_length = sum(len(attr) for attr in attributes) / len(attributes) if attributes else 0
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted([
            'html document',
            document_type,
            title.lower(),
            f'{document_length} characters',
            f'{unique_classes} unique classes',
            f'{tag_count} tags',
            f'average attribute length: {round(avg_attr_length, 2)}'
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
            
            # Add additional mathematical operations
            words.append(str(round(math.sin(result), 2)))
            words.append(str(round(math.cos(result), 2)))
        
        # Add the type of the result to the output
        words.append(type(result).__name__)
        
        # Calculate and add the length of the result string
        words.append(f'{len(str(result))} characters')
        
        # If the result is a list or tuple, add its length
        if isinstance(result, (list, tuple)):
            words.append(f'length: {len(result)}')
        
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
        
        # Count the number of punctuation marks
        punctuation_count = sum(c in '.,:;!?()[]{}' for c in input_data)
        words.append(f'{punctuation_count} punctuation marks')
        
        # Calculate the ratio of uppercase to lowercase letters
        upper_count = sum(c.isupper() for c in input_data)
        lower_count = sum(c.islower() for c in input_data)
        case_ratio = upper_count / lower_count if lower_count > 0 else 0
        words.append(f'uppercase to lowercase ratio: {round(case_ratio, 2)}')
        
        return ','.join(sorted(words))