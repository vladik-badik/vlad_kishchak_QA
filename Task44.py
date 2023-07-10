import xml.etree.ElementTree as ET
import json

def process_element(element):
    locators = []
    for locator in element.findall('locator'):
        platform = locator.get('platform')
        locator_type = locator.get('locator_type')
        value = locator.text
        locators.append({'locator_type': locator_type, 'value': value})
    return {element.get('name'): locators}

def process_page(page):
    elements = {}
    for element in page.findall('element'):
        elements.update(process_element(element))
    return {page.get('name'): elements}

def convert_xml_to_json(xml_file, json_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    pages = {}
    for page in root.findall('page'):
        pages.update(process_page(page))

    with open(json_file, 'w') as f:
        json.dump(pages, f, indent=4)

convert_xml_to_json('pages.xml', 'pages.json')
