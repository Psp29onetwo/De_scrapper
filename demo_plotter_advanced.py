import csv
import matplotlib.pyplot as plt

with open("HP Omen.csv") as csv_file:
    # Phase 1 - Retrieving data from csv file -------------------------------------------------------------------------------
    csv_reader = csv.reader(csv_file)
    listOfAttributes = []
    listOfData = []
    indexOfTitle = 0
    indexOfData = 0
    counter = 0
    for line in csv_reader:
        if counter == 0:
            listOfAttributes = line

        if counter == 1:
            listOfData = line

        counter += 1
    # print(listOfAttributes)
    # print(listOfData)

    for i in range(len(listOfAttributes)):
        if (listOfAttributes[i]) == "title":
            indexOfTitle = i
        if listOfAttributes[i] == "data":
            indexOfData = i

    # print(indexOfTitle, indexOfData)

    titleOfProduct = listOfData[indexOfTitle]
    dataComplexString = listOfData[indexOfData]  # maha kaamni list

    # print(titleOfProduct)
    # print(dataComplexList)

    # Phase 1 complete Havey dataComplexList thi plot banavo----------------------------------------------------------------/

    # Phase 2 Make dataComplexList from dataComplexString-------------------------------------------------------------------------/

    # print(dataComplexList)
    xTimeEncrypted = []
    yPrice = []
    bad_chars = [']', '[']
    for i in bad_chars:
        dataComplexString = dataComplexString.replace(i, '')

    dataComplexList = dataComplexString.split(",")
    intList = []

    for element in dataComplexList:
        intList.append(int(element))

    rows, cols = (62, 2)
    intDataList = [[0 for i in range(cols)] for j in range(rows)]
    counter = 0
    for row in range(0,62):
        for column in range(0,2):
            intDataList[row][column] = intList[counter]
            counter+=1

    listTimeX = []
    listPriceY = []

    for i in range(0,len(intDataList)):
        listTimeX.append(intDataList[i][0])

    print(listTimeX)

    for i in range(0, len(intDataList)):
        listPriceY.append((intDataList[i][1]))

    print(listPriceY)

    plt.plot(listTimeX,listPriceY)
    plt.show()

