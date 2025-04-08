import json
import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis wikipedia page detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics wikipedia page detected"
        elif 'text processing' in input_data.lower():
            return "text processing wikipedia page detected"
        elif 'python' in input_data.lower():
            return "python wikipedia page detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add a prefix
        return f"evaluated: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string or JSON-like structure
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any leading/trailing whitespace from each value
                cleaned_values = [value.strip() for value in sorted_values]
                # Join the cleaned and sorted values
                return f"sorted: {','.join(cleaned_values)}"
            else:
                # Check if the input is a valid number
                try:
                    float(input_data)
                    return f"number: {str(input_data).lower()}"
                except ValueError:
                    # If not a number, attempt to parse as JSON
                    try:
                        json_data = json.loads(input_data)
                        # If JSON parsing succeeds, return a string representation of the JSON
                        return f"json: {json.dumps(json_data, sort_keys=True).lower()}"
                    except json.JSONDecodeError:
                        # If JSON parsing fails, process as a regular string
                        # Reverse the string, capitalize the first letter, and add a prefix
                        reversed_string = input_data[::-1].lower()
                        # Count the number of vowels in the reversed string
                        vowel_count = sum(1 for char in reversed_string if char in 'aeiou')
                        # Count the number of consonants in the reversed string
                        consonant_count = sum(1 for char in reversed_string if char.isalpha() and char not in 'aeiou')
                        
                        # Extract words from the reversed string
                        words = re.findall(r'\b\w+\b', reversed_string)
                        word_count = len(words)
                        
                        return f"processed: {reversed_string.capitalize()} (vowels: {vowel_count}, consonants: {consonant_count}, words: {word_count})"
        else:
            # If input is not a string, convert to string, lowercase, and add a prefix
            return f"converted: {str(input_data).lower()}"