import pickle
import os

urlTree = dict()
dirList = []
figList = []
download_folder = "temp/stp2/_pages"


def get_figs_url(fList: list):
    return


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


if __name__ == '__main__':
    os.system("cls")
    main()
