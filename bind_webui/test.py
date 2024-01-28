def parse_bind_config():
    try:
        # Run named-checkconf to check the BIND configuration
        result = subprocess.run(['named-checkconf', '-p'], capture_output=True, text=True, check=True)
        
        # Parse the output to extract DNS records
        records = []
        for line in result.stdout.split('\n'):
            if line.startswith('zone'):
                # Extract relevant information from the line
                parts = line.split()
                name = parts[1].strip('";')
                type = parts[2]
                value = parts[3].strip(';')

                # Add the record to the list
                records.append({"name": name, "type": type, "value": value})

        # Print records to the console for debugging
        print("Parsed DNS Records:")
        for record in records:
            print(record)

        return records

    except subprocess.CalledProcessError as e:
        print(f"Error running named-checkconf: {e}")
        return []
    except Exception as e:
        print(f"Error parsing BIND configuration: {e}")
        return []
