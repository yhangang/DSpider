#页面处理器，需要自定义

#保存二进制文件
def save_file_binary(file_path, data):
    with open(file_path,'wb') as f:
        f.write(data)
         
#保存文本文件
def save_file_str(file_path, data):
    with open(file_path,'w') as f:
        f.write(data)