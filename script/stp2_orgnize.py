import pickle
import os

urlTree = dict()
dirList = []
download_folder = "downloads/documentation/tutorials"
page_folder = "../jekyll-gitbook/_pages"
jekyll_header_dict = {
    "author": "DoubleCat",
    "date": "2025-04-11",
    "layout": "post"
}


def gen_jekyll_header(info: dict) -> list:
    header = []
    header.append("---\n")
    for key in jekyll_header_dict:
        header.append(f"{key}: {jekyll_header_dict[key]}\n")
    header.append(f"category: {info["category"]}\n")
    header.append(f"title: {info["title"]}\n")
    header.append("---\n\n")
    return header


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
            dirList.append({
                "dir": url + key + ".md",
                "category": father,
                "title": dict_tree["text"]
            })


def main():
    global urlTree
    global fList
    with open('data.pkl', 'rb') as f:
        urlTree = pickle.load(f)
    get_dir(urlTree)
    for item in dirList:
        fList = []
        with open(download_folder+item["dir"], "r", encoding="UTF-8") as r_f:
            fList = r_f.readlines()
            r_f.close()
        with open(page_folder+item["dir"], "w+", encoding="UTF-8") as w_f:
            header = gen_jekyll_header(item)
            for line in header:
                w_f.write(line)
            for line in fList:
                w_f.write(line)
            w_f.close()
        print(f"I: Processed [{item["dir"]}]")


if __name__ == '__main__':
    os.system("cls")
    main()
