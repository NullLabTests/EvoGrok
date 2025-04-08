import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected"
        else:
            # Use regex to extract the title if possible
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"wikipedia {title_match.group(1).lower()} html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # If all values are numbers, return their sum and average
                if all(value.strip().isdigit() for value in sorted_values):
                    numbers = [int(value.strip()) for value in sorted_values]
                    return f"sum: {sum(numbers)}, average: {sum(numbers)/len(numbers):.2f}"
                else:
                    return ','.join(sorted_values)
            elif ' ' in input_data:
                # Sort and join space-separated values
                return ' '.join(sorted(input_data.split()))
            elif input_data.isdigit():
                # If the input is a single number, return its square root and cube root
                number = int(input_data)
                return f"sqrt: {round(number ** 0.5, 2)}, cbrt: {round(number ** (1/3), 2)}"
            else:
                # Reverse the input string, capitalize it, and return it
                return str(input_data)[::-1].capitalize()
        elif isinstance(input_data, (int, float)):
            # If the input is a number, return its factorial and logarithm
            import math
            return f"factorial: {math.factorial(int(input_data))}, log: {math.log(input_data):.2f}"
        else:
            # For other types, return a string representation of the type
            return f"input type: {type(input_data).__name__}"