def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "Wikipedia Data Analysis HTML document detected. Includes various classes and attributes for styling and functionality, related to data analysis techniques and tools."
        elif 'mathematics' in input_data.lower():
            return "Wikipedia Mathematics HTML document detected. Starts with DOCTYPE declaration, contains information about mathematical concepts and theories."
        elif 'text processing' in input_data.lower():
            return "Wikipedia Text Processing HTML document detected. Includes various classes and attributes for styling and functionality, related to text manipulation and analysis techniques."
        else:
            return "Generic HTML document detected. No specific Wikipedia page type identified."
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        output = str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas
            output = ','.join(cleaned_values).lower()
        else:
            # Return the input as a lowercase string
            output = str(input_data).lower()
        
        # Check if the result contains any of the HTML document types
        if 'data analysis' in output:
            output += ", related to Wikipedia Data Analysis HTML document"
        elif 'mathematics' in output:
            output += ", related to Wikipedia Mathematics HTML document"
        elif 'text processing' in output:
            output += ", related to Wikipedia Text Processing HTML document"
    
    # Add additional processing for mathematical expressions
    if isinstance(input_data, str) and all(char in '0123456789+-*/(). ' for char in input_data):
        try:
            # Evaluate the expression again to get the numeric result
            numeric_result = eval(input_data)
            # Add information about the mathematical operation
            if '+' in input_data:
                output += f", result of addition: {numeric_result}"
            elif '-' in input_data:
                output += f", result of subtraction: {numeric_result}"
            elif '*' in input_data:
                output += f", result of multiplication: {numeric_result}"
            elif '/' in input_data:
                output += f", result of division: {numeric_result}"
        except ZeroDivisionError:
            output += ", division by zero attempted"
        except:
            pass  # Ignore other errors, as they were already handled
    
    return output