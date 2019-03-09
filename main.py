import urllib.request, re

def mostWord(source):
    word = {}
    for text in source:
        count = 0
        if text in word.keys():
            count = word[text]
        else:
            word[text] = {}
        word[text] = count + 1

    sorted_list = sorted(word, key=word.get, reverse=True)
    for r in sorted_list:
        print(r, word[r])

while True:
    type = str(input("==============\n1 : url\n2 : file\n3 : exit\n: "))
    if(type == 'exit' or type == '3'):
        break

    if(type=='1'):
        try:
            url = str(input("url:"))
            response = urllib.request.urlopen(url)
            if (response.status == 200):
                source = re.sub(r'<script[\s\S]+?/script>', '', response.read().decode("utf-8"), 0).strip()
                source = re.sub(r'<.*[\s\S]+?>', '', source, 0)
                source = re.sub(r'<.*?>', '', source, 0).split()
        except Exception as ex:
            print('에러가 발생 했습니다', ex)
            pass
        mostWord(source)
    elif(type=='2'):
        break

