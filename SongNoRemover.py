import os, re
#Valid formats to search for
music_format = ['.mp3','.ogg','.flac',
                '.m4a','.wav']

#Regex string: Select everything until first alpha character
reg_search= r'^[^a-zA-Z一-龠ぁ-ゔァ-ヴー々〆〤]*?(?=[a-zA-Z一-龠ぁ-ゔァ-ヴー々〆〤])'
#Search current directory 
for file in os.listdir("./"):
    name, ext = os.path.splitext(file)
    if ext in music_format:
        print('orig: ' + name + '\n' + 'new: ' + re.sub(reg_search,'',name) + '\n----')
        os.rename(name + ext, re.sub(reg_search,'',name) + ext)
print('\nHit enter to close')
input()