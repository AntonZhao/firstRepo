import os
from nt import chdir

def renameF(preName,newName):
    '''
    rename之前要先用chdir()函数进入到目标文件所在的路径，告诉python编译器要重命名的文件在哪儿，然后才可以修改；
　　Python不是可怕的终结者，她其实很幼小，自己找不到文件，需要我们详细又耐心的告诉她该去哪儿找~ 路径通过 os.path.dirname()函数获得：
    '''
    chdir(os.path.dirname(preName))
    os.rename(preName,newName)

def readTxt(path):  #读取文本中新文件名
    file_object = open(path, "r", encoding='UTF-8')
    lines = file_object.readlines()
    file_object.close()
    return lines

if __name__ == '__main__':
    path = "D:\核桃编程\视频录制"
    newNameFile = "D:\核桃编程\视频录制\\fileName.txt"
    newName = readTxt(newNameFile)
    print(newName)

    print(os.listdir(path))

    num = 0

    for file in os.listdir(path):
        if file[-3:] == 'mp4':
            newFileName = newName[num].replace('\n', '') + ".mp4"
            filePre = path + '\\' + file
            fileNew = path + '\\'+ newFileName
            renameF(filePre,fileNew)
            num += 1
