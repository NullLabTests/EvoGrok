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
        words = set(re.findall(r'\b\w+\b', input_data.lower()))
        words.discard('doctype')
        words.discard('html')
        
        # Calculate the length of the processed HTML content
        html_length = len(''.join(c.lower() if c.isalnum() else ' ' for c in input_data))
        
        # Count the number of class attributes
        class_count = len(re.findall(r'class\s*=\s*["\'][^"\']*["\']', input_data, re.IGNORECASE))
        
        # Return a sorted, comma-separated list of detected elements, document type, and length
        return ','.join(sorted(['html document', document_type, f'html length: {html_length}', 
                                f'class attributes: {class_count}'] + list(words)))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result: convert to string, split into words, remove non-alphanumeric characters
        processed_result = ''.join(c.lower() if c.isalnum() else ' ' for c in str(result))
        words = processed_result.split()
        
        # Calculate the sum of numeric values in the result
        numeric_sum = sum(float(word) for word in words if word.replace('.', '').isdigit())
        
        # Calculate the length of the processed result
        result_length = len(processed_result)
        
        # Calculate the number of unique words
        unique_word_count = len(set(words))
        
        # Return a sorted, comma-separated list of processed words, numeric sum, result length, and unique word count
        return ','.join(sorted(words + [f'numeric sum: {numeric_sum:.2f}', f'result length: {result_length}', 
                                        f'unique words: {unique_word_count}']))
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, remove non-alphanumeric characters, split into words, and sort
        processed_input = ''.join(c.lower() if c.isalnum() else ' ' for c in str(input_data))
        words = processed_input.split()
        
        # Calculate the length of the processed input
        input_length = len(processed_input)
        
        # Calculate the number of unique words
        unique_word_count = len(set(words))
        
        # Calculate the average word length
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        
        # Return a sorted, comma-separated list of processed words, input length, unique word count, and average word length
        return ','.join(sorted(words + [f'input length: {input_length}', f'unique words: {unique_word_count}', 
                                        f'average word length: {avg_word_length:.2f}']))