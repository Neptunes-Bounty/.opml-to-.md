import xml.etree.ElementTree as ET
import argparse

def opml_to_markdown(opml_file, md_file):
    tree = ET.parse(opml_file)
    root = tree.getroot()

    with open(md_file, 'w', encoding='utf-8') as md:
        for outline in root.findall(".//outline"):
            process_outline(outline, md, level=0)

def process_outline(element, md_file, level):
    text = element.get("text", "").strip()
    if text:
        md_file.write("  " * level + "- " + text + "\n")

    for child in element.findall("outline"):
        process_outline(child, md_file, level + 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Dynalist OPML to Markdown")
    parser.add_argument("input", help="Path to the input OPML file")
    parser.add_argument("output", help="Path to the output Markdown file")

    args = parser.parse_args()
    opml_to_markdown(args.input, args.output)

    print(f"Conversion complete: {args.output}")