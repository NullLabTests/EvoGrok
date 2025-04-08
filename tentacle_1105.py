import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Detect specific types of Wikipedia HTML documents
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input and 'lang="en"' in lowercase_input:
            return "wikipedia english text processing html document detected"
        else:
            # Attempt to extract the title from the HTML
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).lower()
                # Check for specific Wikipedia page types
                if 'wikipedia' in lowercase_input and 'lang="en"' in lowercase_input:
                    return f"wikipedia {title} html document detected"
                else:
                    return f"generic {title} html document detected"
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
                # Calculate and return the sum and average of the numbers
                numbers = [float(value) for value in cleaned_values]
                return f"sum: {sum(numbers)}, average: {sum(numbers)/len(numbers)}, sorted: {result}"
            else:
                return result
        else:
            # Convert to lowercase and remove extra whitespace
            cleaned_input = re.sub(r'\s+', ' ', input_data.lower()).strip()
            
            # Check for specific patterns
            if cleaned_input.startswith('wikipedia: '):
                return f"wikipedia page detected: {cleaned_input[11:]}"
            elif re.match(r'^https?://', cleaned_input):
                return f"url detected: {cleaned_input}"
            elif re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', cleaned_input):
                return f"email address detected: {cleaned_input}"
            # Check if the input looks like a date
            elif re.match(r'^\d{4}-\d{2}-\d{2}$', cleaned_input):
                return f"date detected: {cleaned_input}"
            # Check if the input looks like a time
            elif re.match(r'^\d{2}:\d{2}(:\d{2})?$', cleaned_input):
                return f"time detected: {cleaned_input}"
            else:
                return cleaned_input