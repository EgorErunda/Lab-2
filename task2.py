import xml.etree.ElementTree as ET

DATA = "currency.xml"

def scraping(Data):
  tree = ET.parse(Data)
  root = tree.getroot()
  ans = {}
  valutes = root.findall('Valute')

  for val in valutes:
      Name = val.find('Name').text
      Value = val.find('Value').text
      ans[Name] = Value
  return ans


if __name__ == '__main__':
  result = scraping(DATA)
  print(result)