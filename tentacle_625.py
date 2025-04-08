import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected"
        else:
            # If no specific type is detected, check for other keywords
            if 'wikipedia' in input_data.lower():
                return "wikipedia generic html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and remove extra whitespace
        processed_result = re.sub(r'\s+', ' ', str(result).lower()).strip()
        
        # If the result is a number, round it to 2 decimal places
        try:
            return f"{float(processed_result):.2f}"
        except ValueError:
            return processed_result
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove extra whitespace from each value and lowercase it
            cleaned_values = [re.sub(r'\s+', ' ', value.strip().lower()) for value in sorted_values]
            return ','.join(cleaned_values)
        else:
            # Convert to lowercase, remove extra whitespace, and replace multiple spaces with a single space
            processed_input = re.sub(r'\s+', ' ', input_data.lower()).strip()
            
            # Check if the processed input looks like a URL
            if re.match(r'^https?://', processed_input):
                return f"url detected: {processed_input}"
            else:
                return processed_input