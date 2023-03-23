from xml.etree import ElementTree

# работа с xml на чтение
tree = ElementTree.parse("file name")  # создание дерева с передачей ему имени xml файла
root = tree.getroot()  # получение корня дерева
for element in root.iter("scores"):  # поиск тега со значением scores
    for elem in element:  # перебор всех элементов внутри тега scores
        pass

# работа с xml на запись
root[0].iter("module1").text = "new score in module1"  # изменение значения в теге module1
# первого тега из корня
desc = ElementTree.Element("description")  # создание нового тега, который надо создать
desc.text = "some text"  # изменение атрибута text
root[0].append(desc)  # добавление нового тега в необходимую часть файла
tree.write("file name")  # запись всех изменений
