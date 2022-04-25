import xmltodict


def handle_xml_file(xml_file) -> dict:
    """
    Read xml file and convert it into a dict.
    @param xml_file: InMemoryUploadedFile
    @return: A dict who depicts the previous xml file.
    """
    content_file = xml_file.read()

    if is_xml_valid(content_file):
        xml_converted = xmltodict.parse(content_file)
        return {k: v if v is not None else '' for k, v in xml_converted.items()}
    else:
        return {'Message': 'Invalid XML'}


def is_xml_valid(xml_file: str) -> bool:
    """
    XML is valid or not
    """

    import xml.etree.ElementTree as elementTree
    try:
        is_valid = elementTree.fromstring(xml_file)
        return True
    except:
        return False
