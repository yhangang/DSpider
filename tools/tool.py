
#将url中不符合文件命名规则的字符替换掉
def url_replace(str):
    str = str.replace(':', '!')
    str = str.replace('/', "!")
    str = str.replace('\\', "!")
    str = str.replace('|', "!")
    str = str.replace('*', '!')
    str = str.replace('?', "!")
    str = str.replace('<', "!")
    str = str.replace('>', "!")
    str = str.replace('"', "!")
    return str