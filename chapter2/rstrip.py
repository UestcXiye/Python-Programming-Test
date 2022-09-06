language="python "
print(language)
print(language.rstrip()) # rstrip() 方法删除 string 字符串末尾的指定字符，默认为空白符，包括空格、换行符、回车符、制表符。
print(language) # 删除只是暂时的，并不改变原字符串的内容
# 需要将删除操作的结果存回变量中，才能永久删除这个字符串的空白
language=language.rstrip()
print(language)