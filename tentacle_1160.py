import json
import re

def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Detect specific types of HTML documents based on known patterns
        if re.search(r'data analysis', input_str):
            return "data analysis html document detected"
        elif re.search(r'mathematics', input_str):
            return "mathematics html document detected"
        elif re.search(r'text processing', input_str):
            return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, check for JSON-like structure
        try:
            # Attempt to parse as JSON
            json_data = json.loads(input_str)
            # If successful, return a string representation of the JSON
            return json.dumps(json_data, sort_keys=True)
        except json.JSONDecodeError:
            # If JSON parsing fails, process as a comma-separated list or return as is
            if ',' in input_str:
                # Split, sort, and join the list
                sorted_list = sorted(input_str.split(','))
                # Remove any empty strings that might result from leading/trailing commas
                cleaned_list = [item.strip() for item in sorted_list if item.strip()]
                return ','.join(cleaned_list)
            else:
                # If no commas, check for specific keywords
                if re.search(r'data analysis', input_str):
                    return "data analysis text detected"
                elif re.search(r'mathematics', input_str):
                    return "mathematics text detected"
                elif re.search(r'text processing', input_str):
                    return "text processing text detected"
                else:
                    # If no specific keywords, check for mathematical expressions
                    math_pattern = r'\d+(\.\d+)?\s*[\+\-\*\/]\s*\d+(\.\d+)?'
                    if re.search(math_pattern, input_str):
                        try:
                            # Attempt to evaluate as a simple mathematical expression
                            result = eval(input_str)
                            return f"simple math result: {str(result).lower()}"
                        except:
                            # If evaluation fails, return the input as is
                            return input_str
                    else:
                        # If no math pattern, return the input as is
                        return input_str