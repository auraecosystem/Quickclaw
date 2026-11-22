import xml.etree.ElementTree as ET

root = ET.Element("TestSuite", name="FileValidationSuite")

cases = [
    ("Test_01", "sample.txt", "200"),
    ("Test_02", "corrupt.txt", "400"),
]

for test_id, filename, expected_code in cases:
    tc = ET.SubElement(root, "TestCase", id=test_id)
    ET.SubElement(tc, "InputFile").text = filename
    ET.SubElement(tc, "ExpectedStatus").text = expected_code

tree = ET.ElementTree(root)
ET.indent(tree, space="  ")
tree.write("files.tst", encoding="utf-8", xml_declaration=True)
