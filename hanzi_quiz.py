import random
import unicodedata


def remove_accents(text):
    return ''.join(
        char for char in unicodedata.normalize('NFD', text)
        if unicodedata.category(char) != 'Mn'
    )


learned_hanzi = ["的","一","是","不","了","人","我","在","有","他",
                 "这","为","之","大","来","以","个","中","上","们",
                 "到","说","国","和","地","也","子","时","道","出",
                 "而","要","于",'七','谢','后','怎','四','电',
                 '今','少','岁','爸','喜','九','饭', '叫','先',
                 '商','姐','京','衣','上','我','钟','昨','没',
                 '见', '工', '儿', '果', '住', '视', '太', '觉', '想', 
                 '和', '大', '话', '时', '西', '热', '爱', '八', '样','写',
                 '再', '喂', '哪', '师', '分', '脑', '你', '谁'
                 ]

learned_pinyin = [
 "de","yī","shì","bù","le","rén","wǒ","zài","yǒu","tā",
 "zhè","wèi","zhī","dà","lái","yǐ","gè","zhōng","shàng","men",
 "dào","shuō","guó","hé","dì","yě","zǐ","shí","dào","chū",
 "ér","yào","yú","qī","xiè","hòu","zěn","sì","diàn",
 "jīn","shǎo","suì","bà","xǐ","jiǔ","fàn","jiào","xiān",
 "shāng","jiě","jīng","yī","shàng","wǒ","zhōng","zuó","méi",
 "jiàn","gōng","ér","guǒ","zhù","shì","tài", "jué/jiào", "xiǎng",
"hé", "dà", "huà", "shí", "xī", "rè", "ài", "bā", "yàng", "xiě", 
"zài", "wèi", "nǎ",  "shī", "fēn", "nǎo",  "nǐ", "shéi"
]

normalized_pinyin = [remove_accents(word) for word in learned_pinyin]

hanzi_pinyin_dict = dict(zip(learned_hanzi, learned_pinyin))

normalize_hanzi_pinyin_dict = dict(zip(learned_hanzi, normalized_pinyin))

key_list = list(hanzi_pinyin_dict.keys())
value_list = list(hanzi_pinyin_dict.values())

randomized_keys = random
correct= 0
incorrect = []


counter = 0

c = len(key_list) # change c to choose the number of characters to study....to study all, change c to len(key_list)

random_key_list = random.sample(key_list, len(key_list))

# for x in random.sample(key_list, len(key_list)): #uncomment this line if you want to study all of the characters
for x in random_key_list[:c]: 
    counter+=1
    answer=input('Hanzi: '+ str(x)+ ' Pinyin: ')
    print('')
    if answer == normalize_hanzi_pinyin_dict[x]:
        print(hanzi_pinyin_dict[x]+ ' is correct')
        print('')
        correct+=1
    else:
        print('')
        print('That is incorrect. The answer is ' + hanzi_pinyin_dict[x])
        incorrect.append(x)
        print('')


score = (correct/counter)*100

if score == 100:
    print('')
    print('Congratulations you scored 100%')
    exit()
else:
    print('')
    print('you scored ' + str(score))
    pass

difficult_hanzi = input('do you want to practice the ones you missed? type: yes or no ')

very_hard_dict = {}

if difficult_hanzi== 'no':
    score = (correct/len(learned_hanzi))*100
    print('')
    print('your final score is '+ str(score) + ' %') 
else:
    for x in random.sample(incorrect, len(incorrect)):
        counter +=1
        answer=input('Hanzi: '+ str(x)+ ' Pinyin: ')
        if answer == normalize_hanzi_pinyin_dict[x]:
            print('')
            print(hanzi_pinyin_dict[x]+ ' is correct')
            correct+=1
        else:
            print('')
            print('That is incorrect. The answer is ' + hanzi_pinyin_dict[x])
            very_hard_dict[x]= hanzi_pinyin_dict[x]

print("")
print("")
print('Need to study the following:')
print("")
print(very_hard_dict)

very_hard_list = []

for x in very_hard_dict:
    very_hard_list.append([x, very_hard_dict[x]])



with open("practice.txt", "w", encoding= "utf-8") as file:
    for x in very_hard_list:
        file.write(str(x[0]) + ": " + str(x[1]) + "\n")
        

score = (correct/counter)*100
print('')
print('your final score is '+ str(score) + ' %') 


