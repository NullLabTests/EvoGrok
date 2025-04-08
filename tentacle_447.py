import math
import re

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
        
        # Extract and process words from the HTML content
        words = set()
        for word in re.findall(r'\b\w+\b', input_data.lower()):
            if word.isalnum():
                words.add(word)
        
        # Extract numbers from the HTML content
        numbers = [float(num) for num in re.findall(r'\b-?\d+(\.\d+)?\b', input_data)]
        
        # Calculate statistics on the numbers
        if numbers:
            avg = sum(numbers) / len(numbers)
            max_num = max(numbers)
            min_num = min(numbers)
            stats = [f'avg:{round(avg, 2)}', f'max:{round(max_num, 2)}', f'min:{round(min_num, 2)}']
        else:
            stats = []
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted(['html document', document_type] + list(words) + stats))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result: convert to string, split into words, remove non-alphanumeric
        words = [word for word in str(result).lower().split() if word.isalnum()]
        
        # If the result is a number, add its square root and cube root to the output
        if isinstance(result, (int, float)):
            words.append(str(round(math.sqrt(abs(result)), 2)))
            words.append(str(round(math.pow(abs(result), 1/3), 2)))
        
        # Return a sorted, comma-separated list of processed words
        return ','.join(sorted(words))
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, remove non-alphanumeric, sort, and join with commas
        words = [word for word in str(input_data).lower().split() if word.isalnum()]
        
        # Extract numbers from the input
        numbers = [float(num) for num in re.findall(r'\b-?\d+(\.\d+)?\b', input_data)]
        
        # Calculate statistics on the numbers
        if numbers:
            avg = sum(numbers) / len(numbers)
            max_num = max(numbers)
            min_num = min(numbers)
            stats = [f'avg:{round(avg, 2)}', f'max:{round(max_num, 2)}', f'min:{round(min_num, 2)}']
        else:
            stats = []
        
        return ','.join(sorted(words + stats))