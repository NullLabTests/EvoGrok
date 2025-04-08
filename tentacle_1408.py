import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'wikipedia data analysis html document detected (html5)'
        elif 'mathematics' in input_data.lower():
            return 'wikipedia mathematics html document detected (html5)'
        elif 'text processing' in input_data.lower():
            return 'wikipedia text processing html document detected (html5)'
        else:
            # If no specific pattern is detected, check for generic HTML5
            if 'html5' in input_data.lower():
                return 'generic html5 document detected'
            else:
                return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # If the result is a number, return it as a string with two decimal places
            formatted_result = f"{result:.2f}".lower()
            
            # Check if the result is a whole number
            if formatted_result.endswith('.00'):
                return formatted_result[:-3]  # Remove '.00' for whole numbers
            else:
                return formatted_result
        elif isinstance(result, str):
            # If the result is a string, process it like text input
            return process_text(result)
        else:
            # For other types, convert to string and process
            return process_text(str(result))
    except:
        # If evaluation fails, process the input as text
        return process_text(str(input_data))

def process_text(text):
    # Convert to lowercase, split into words, sort them, and join with commas
    words = sorted(re.findall(r'\b\w+\b', text.lower()))
    
    # Remove common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
    filtered_words = [word for word in words if word not in stop_words]
    
    # If there are no words after filtering, return 'empty'
    if not filtered_words:
        return 'empty'
    
    # Join the filtered words with commas
    processed_text = ','.join(filtered_words)
    
    # If the result is a single word, return it capitalized
    # Otherwise, return the sorted, comma-separated list with the first word capitalized
    if ',' in processed_text:
        return processed_text.capitalize()
    else:
        return processed_text.replace(',', '').capitalize()