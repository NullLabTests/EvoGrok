def tentacle(input_data):
    # Function to detect and categorize HTML documents
    def detect_html_category(html_content):
        html_content = html_content.lower()
        if 'data analysis' in html_content:
            return "data analysis html document detected"
        elif 'mathematics' in html_content:
            return "mathematics html document detected"
        elif 'text processing' in html_content:
            return "text processing html document detected"
        else:
            return "generic html document detected"

    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        return detect_html_category(input_data)

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Split and process comma-separated values
            values = input_data.split(',')
            processed_values = []

            for value in values:
                value = value.strip()
                if value:
                    if value.lower().startswith('<!doctype'):
                        processed_values.append(detect_html_category(value))
                    else:
                        try:
                            # Attempt to evaluate each value as a mathematical expression
                            eval_result = eval(value)
                            processed_values.append(str(eval_result).lower())
                        except:
                            # If evaluation fails, process as a string
                            processed_values.append(value.lower())

            # Sort and join the processed values
            return ','.join(sorted(processed_values))
        else:
            # Convert the input to lowercase and remove leading/trailing whitespace
            return input_data.strip().lower()