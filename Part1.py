import xml.etree.ElementTree as ET
import pathlib
import sys
import pandas as pd

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')




def exportdataExcel(dirList, path):
    try:
        nameList = []
        dataList = []
        verdictList = []
        for dirs in dirList:
            dirname = path + "/" + dirs + "/tc_log.xml"
            tree = ET.parse(dirname)
            print(dirname)
            # get the parent tag
            root = tree.getroot()
            # print the root (parent) tag along with its memory location

            for i in root.findall("TCASE"):
                nameList.append(i.findtext("NAME"))
                print(i.findtext("NAME"))
                dataList.append(i.findtext("DATE"))
                verdictList.append(i.findtext("VERDICT"))
        df = pd.DataFrame({'TestCase': nameList, 'Date': dataList, 'Status': verdictList})
        df.to_excel(writer, sheet_name="Sheet1")
        writer.save()
        # print(nameList,dataList,verdictList)

    except Exception as ez:
        print(ez)


def list_dir(dir):
    path = pathlib.Path(dir)
    dir = []
    try:
        for item in path.iterdir():
            itemdataList = False
            for itemdata in item.iterdir():
                if itemdata.name.split("/")[-1] == "tc_log.xml":
                    itemdataList = True
            if itemdataList:
                if item.name.split("/")[-1] in ['A2DP', 'BAS', 'DID', 'DIS', 'HFP']:
                    dir.append(item.name.split("/")[-1])
        return dir
    except FileNotFoundError:
        print('Invalid directory')


def main():
    path = sys.argv
    path = path[1]
    path = path.replace("\\", "/")
    print(path)
    dirList = list_dir(path)
    print(dirList)
    exportdataExcel(dirList, path)


main()
