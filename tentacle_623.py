import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input and 'lang="en"' in lowercase_input:
            return "wikipedia english text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove extra whitespace from each value
            cleaned_values = [re.sub(r'\s+', ' ', value).strip() for value in sorted_values]
            # Join the cleaned values
            result = ','.join(cleaned_values)
            
            # Check if the result looks like a list of numbers
            if all(re.match(r'^-?\d+(\.\d+)?$', value) for value in cleaned_values):
                # Calculate and return the sum of the numbers
                return f"sum: {sum(float(value) for value in cleaned_values)}"
            else:
                return result
        else:
            # Convert to lowercase and remove extra whitespace
            cleaned_input = re.sub(r'\s+', ' ', input_data.lower()).strip()
            
            # Check if the input looks like a Wikipedia page title
            if cleaned_input.startswith('wikipedia: '):
                return f"wikipedia page detected: {cleaned_input[11:]}"
            else:
                return cleaned_input