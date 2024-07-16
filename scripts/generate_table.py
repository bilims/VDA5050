import json
import sys


def generate_markdown_table(schema, output_file):
    table_header = "| **Field** | **Type** | **Description** | **Predefined Values** | **Example Value** |\n"
    table_header += "|-----------|----------|-----------------|----------------------|-------------------|\n"

    def parse_properties(properties, parent=""):
        rows = []
        for field, attributes in properties.items():
            field_name = f"{parent}.{field}" if parent else field
            if "enum" in attributes:
                field_type = "Enum"
                enum_values = ", ".join(attributes["enum"])
            else:
                field_type = attributes.get("type", "Unknown")
                if isinstance(field_type, list):
                    field_type = "/".join(field_type)
                enum_values = ""
            description = attributes.get("description", "No description available.")
            example_value = ", ".join(map(str, attributes.get("examples", [])))
            rows.append(
                f"| `{field_name}` | {field_type.capitalize()} | {description} | {enum_values} | {example_value} |"
            )
            if "properties" in attributes:
                rows.extend(parse_properties(attributes["properties"], field_name))
            if "items" in attributes and "properties" in attributes["items"]:
                rows.extend(
                    parse_properties(
                        attributes["items"]["properties"], f"{field_name}[]"
                    )
                )
        return rows

    def parse_schema(schema):
        rows = []
        if "properties" in schema:
            rows.extend(parse_properties(schema["properties"]))
        if "definitions" in schema:
            for definition in schema["definitions"].values():
                if "properties" in definition:
                    rows.extend(parse_properties(definition["properties"]))
        if "components" in schema:
            for component in schema["components"].get("schemas", {}).values():
                if "properties" in component:
                    rows.extend(parse_properties(component["properties"]))
        return rows

    table_rows = parse_schema(schema)
    if not table_rows:  # Additional check for nested schemas
        for key, value in schema.items():
            if isinstance(value, dict) and "properties" in value:
                table_rows.extend(parse_properties(value["properties"]))
    table_content = "\n".join(table_rows)

    with open(output_file, "w") as f:
        f.write(table_header + table_content)


def main(input_files):
    for input_file in input_files:
        print(f"Processing file: {input_file}")  # Debug print
        with open(input_file, "r") as file:
            schema = json.load(file)
        output_file = input_file.replace(".schema", "_table.md")
        generate_markdown_table(schema, output_file)
        print(f"Generated markdown table for {input_file} as {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_table.py <schema_file1> [<schema_file2> ...]")
    else:
        main(sys.argv[1:])
