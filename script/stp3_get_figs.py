from DrissionPage import ChromiumPage, SessionPage
import pickle
import os
import time
import re

urlTree = dict()
dirList = []
figList = []
baseURL = "https://circos.ca"
tutorialsURL = baseURL + "/documentation/tutorials"
download_folder = "temp/stp2/_pages"
figPattern = r'!\[(.*?)\]\((.*?)\)'


def get_figs_url(fList: list):
    for index in range(len(fList)):
        condition_figure = True if fList[index].startswith("![") else False
        if condition_figure:
            figDict = re.findall(figPattern, fList[index])
            for idx, (title, link) in enumerate(figDict, 1):
                figList.append(link)


def get_dir(dict_tree: dict, father: str = "", url: str = "/"):
    for key in dict_tree["chrild"].keys():
        if len(dict_tree["chrild"][key]["chrild"].keys()) > 0:
            if key == "tutorials" or key == "documentation":
                get_dir(
                    dict_tree["chrild"][key],
                    "",
                    "/"
                )
            else:
                get_dir(
                    dict_tree["chrild"][key],
                    key,
                    url + key + "/"
                )
        else:
            dirList.append(url + key)


def main():
    global urlTree
    page = ChromiumPage()
    with open('data.pkl', 'rb') as f:
        urlTree = pickle.load(f)
    get_dir(urlTree)
    for item in dirList:
        dir = os.path.dirname(download_folder+item+".md")
        if not os.path.exists(dir):
            try:
                os.makedirs(dir)
            except BaseException as e:
                print(f"E: Get error [{e}]")

        with open(download_folder+item+".md", "r", encoding="UTF-8") as r_f:
            get_figs_url(r_f.readlines())
            r_f.close()

    for fig in figList:
        figPath = os.path.dirname(download_folder+fig)
        figName = os.path.basename(download_folder+fig)
        print(figPath, figName)
        if not os.path.exists(figPath):
            try:
                os.makedirs(dir)
            except BaseException as e:
                print(f"E: Get error [{e}]")
        if os.path.isfile(download_folder+fig):
            os.remove(download_folder+fig)

        try:
            page.get(tutorialsURL+fig)
            # page.set.download_path(figPath)
            # page.set.download_file_name(figName)
            figEle = page.ele('tag:img')
            figEle.save(figPath)
        except Exception as e:
            print(f"E: Get error[{str(e)}]")
        time.sleep(2)
    page.close()


if __name__ == '__main__':
    os.system("cls")
    main()
