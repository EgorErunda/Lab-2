import csv

DATASET_PATH = 'books-en.csv'

#1
def len_str(Data):
  Data.seek(0)
  reader = csv.DictReader(Data, delimiter = ';')
  counter = 0
  for i in reader:
      if len(i["Book-Title"]) > 30:
          counter += 1
  return counter
#2
def author_poisk(Data, avtor)          :
  Data.seek(0)
  result = []
  reader = csv.DictReader(Data, delimiter = ';')
  for i in reader:
    if i["Book-Author"] == avtor and (int(i["Price"]) < 150):
      result.append(i["Book-Title"])
  return result
#3
def generator(Data):
  Data.seek(0)
  reader =csv.DictReader(Data, delimiter = ';')
  counter = 0
  with open('generator.txt', 'w') as f:
     for i in reader:
        counter += 1
        f.write(f"""{i["Book-Author"]}. {i["Book-Title"]} - {i["Year-Of-Publication"]}\n)""")
        if counter == 20:
           break


if __name__ == "__main__":
       with open(DATASET_PATH) as dataset:
        print(len_str(dataset))
        print(author_poisk(dataset, "Classical Mythology"))
        generator(dataset)
   
