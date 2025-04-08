def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        input_lower = input_data.lower()
        if 'data analysis' in input_lower:
            return "Wikipedia Data Analysis HTML document detected - This document likely contains information about statistical methods and data processing techniques. It may include class attributes and metadata settings that configure the page's appearance."
        elif 'mathematics' in input_lower:
            return "Wikipedia Mathematics HTML document detected - This document covers various mathematical concepts and theories. It starts with a DOCTYPE declaration and may include further elements specific to mathematical content."
        elif 'text processing' in input_lower:
            return "Wikipedia Text Processing HTML document detected - This document discusses methods for manipulating and analyzing text data. It includes classes and attributes that define the styling and functionality of the page."
        else:
            return "Generic HTML document detected - This document may contain various types of content."

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"Mathematical expression evaluated: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas
            result = ','.join(cleaned_values).lower()
        else:
            # Return the input as a lowercase string
            result = str(input_data).lower()
        
        # Check if the result contains any of the HTML document types
        if 'data analysis' in result:
            return f"{result}, related to Wikipedia Data Analysis HTML document - This document likely contains information about statistical methods and data processing techniques."
        elif 'mathematics' in result:
            return f"{result}, related to Wikipedia Mathematics HTML document - This document covers various mathematical concepts and theories."
        elif 'text processing' in result:
            return f"{result}, related to Wikipedia Text Processing HTML document - This document discusses methods for manipulating and analyzing text data."
        else:
            return result