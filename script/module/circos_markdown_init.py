import os
import re

codeBlockSign = "    \n"
figPattern = r'!\[(.*?)\]\((.*?)\)'


def clean_header(fList: list) -> list:
    lession_mainBegin = None
    img_mainBegin = None
    config_mainBegin = None
    for index in range(len(fList)):
        if fList[index].startswith("[Lesson]"):
            lession_mainBegin = index + 1
        if fList[index].startswith("[Images]"):
            img_mainBegin = index + 1
        if fList[index].startswith("[Configuration]"):
            config_mainBegin = index + 1
            break
    if config_mainBegin != None:
        return fList[config_mainBegin + 1:]
    elif img_mainBegin != None:
        return fList[img_mainBegin + 1:]
    elif lession_mainBegin != None:
        return fList[lession_mainBegin + 1:]
    else:
        for index in range(len(fList)):
            if fList[index].startswith("## "):
                config_mainBegin = index + 1
                break
        if config_mainBegin != None:
            return fList[config_mainBegin + 1:]
        else:
            raise ValueError("Can't find begin in the main!")


def figure_clean(fList: list) -> list:
    oList = []
    for index in range(len(fList)):
        condition_figure = True if fList[index].startswith("![") else False
        if condition_figure:
            figDict = re.findall(figPattern, fList[index])
            for idx, (title, link) in enumerate(figDict, 1):
                oList.append(
                    f"![{title}]({link.replace("/documentation/tutorials", "")})\n")
        else:
            oList.append(fList[index])
    return oList


def main_clean(fList: list) -> list:
    oList = []
    codeBlockStartFlag = False
    codeBlockEndFlag = False
    for index in range(0, len(fList) - 1, 1):
        condition_sameSegment = False
        # Conditions (very important: can't trans order)
        condition_codeBlock = True if (
            fList[index] == codeBlockSign and fList[index+1] == codeBlockSign) else False
        condition_special = True if fList[index][0] in [
            '#', '+', '-', '|'] else False
        condition_level = True if condition_special and fList[index][0] == '#' else False
        if not (codeBlockStartFlag or condition_special):
            if (fList[index] != "\n" and fList[index+1] != "\n"):
                if "\n" in fList[index]:
                    condition_sameSegment = True
        if codeBlockStartFlag:
            if (fList[index] == codeBlockSign and fList[index+1] == "\n"):
                codeBlockStartFlag = False
                codeBlockEndFlag = True

        # Process
        if condition_codeBlock:
            codeBlockStartFlag = True
            oList.append("```")
            index += 1
        elif codeBlockEndFlag:
            oList.append("```")
            codeBlockEndFlag = False
        elif condition_sameSegment:
            oList.append(fList[index][:-1])
        elif condition_level:
            oList.append('#' + fList[index][:-1])
        else:
            oList.append(fList[index])

    return oList


def init(fList: list) -> list:
    return main_clean(clean_header(fList))


if __name__ == '__main__':
    print("This is a module, nothing here by run directly.")
    exit(0)
