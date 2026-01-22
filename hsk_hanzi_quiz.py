from pypinyin import pinyin, Style
import unicodedata
import random

again = 0

def remove_accents(text):
    return ''.join(
        char for char in unicodedata.normalize('NFD', text)
        if unicodedata.category(char) != 'Mn'
    )


def hsk1_quiz():
    hsk1_words = ['爱', '八', '爸爸', '杯子', '北京', '本', '不客气', '不', '菜', '茶',
              '吃', '出租车', '打电话', '大', '的', '点', '电脑', '电视', '电影', 
              '东西', '都', '读', '对不起', '多', '多少', ' 儿子', '二', '饭店', 
              '飞机', '分钟', '高兴', '个', '工作', '狗', '汉语', '好', '号', '喝', 
              '和', '很', '后面', '回', '会', '几', '家', '叫', '今天', '九', '开', 
              '看', '看见', '块', '来', '老师', '了', '冷', '里', '六', '吗', '妈妈', 
              '买', '猫', '没关系', '没有', '米饭', '名字', '明天', '哪', '哪儿', '那', 
              '呢', '能', '你', '年', '女儿', '朋友', '漂亮', '苹果', '七', '前面', '钱', 
              '请', '去', '热', '人', '认识', '三', '商店', '上', '上午', '少', '谁', '什么', 
              '十', '时候', '是', '书', '水', '水果', '睡觉', '说', '四', '岁', '他', 
              '她', '太', '天气', '听', '同学', '喂', '我', '我们', '五', '喜欢', '下', 
              '下午', '下雨', '先生', '现在', '想', '小', '小姐', '些', '写', '谢谢', 
              '星期', '学生', '学习', '学校', '一', '一点儿', '医生', '医院', '衣服', 
              '椅子', '有', '月', '再见', '在', '怎么', '怎么样', '这', '中国', '中午', 
              '住', '桌子', '字', '昨天', '做', '坐']

    hsk1_pinyin = []

    for hanzi in hsk1_words:
        pinyin_word = ' '.join([s[0] for s in pinyin(hanzi, style=Style.TONE)])
        hsk1_pinyin.append(pinyin_word)

    hsk1_normalized_pinyin = [remove_accents(word) for word in hsk1_pinyin]

    hsk1_hanzi_pinyin_dict = dict(zip(hsk1_words, hsk1_pinyin))

    normalize_hsk1_hanzi_pinyin_dict = dict(zip(hsk1_words, hsk1_normalized_pinyin))

    hsk1_key_list = list(hsk1_hanzi_pinyin_dict.keys())
    hsk1_value_list = list(hsk1_hanzi_pinyin_dict.values())

    correct= 0
    incorrect = []
    

    counter = 0

    # c = len(hsk1_key_list) # change c to choose the number of characters to study....to study all, change c to len(key_list)
    c = 5


    random_key_list = random.sample(hsk1_key_list, len(hsk1_value_list))

    # for x in random.sample(key_list, len(key_list)): #uncomment this line if you want to study all of the characters
    for x in random_key_list[:c]: 
        counter+=1
        answer=input('Hanzi: '+ str(x)+ ' Pinyin: ')
        print('')
        if answer == normalize_hsk1_hanzi_pinyin_dict[x]:
            print(hsk1_hanzi_pinyin_dict[x]+ ' is correct')
            print('')
            correct+=1
        else:
            print('')
            print('That is incorrect. The answer is ' + hsk1_hanzi_pinyin_dict[x])
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
        score = (correct/len(hsk1_words))*100
        print('')
        print('your final score is '+ str(score) + ' %') 
    else:
        for x in random.sample(incorrect, len(incorrect)):
            counter +=1
            answer=input('Hanzi: '+ str(x)+ ' Pinyin: ')
            if answer == normalize_hsk1_hanzi_pinyin_dict[x]:
                print('')
                print(hsk1_hanzi_pinyin_dict[x]+ ' is correct')
                correct+=1
            else:
                print('')
                print('That is incorrect. The answer is ' + hsk1_hanzi_pinyin_dict[x])
                very_hard_dict[x]= hsk1_hanzi_pinyin_dict[x]

    print("")
    print("")
    print('Need to study the following:')
    print("")
    print(very_hard_dict)

    very_hard_list = []

    for x in very_hard_dict:
        very_hard_list.append([x, very_hard_dict[x]])



    # with open("practice.txt", "w", encoding= "utf-8") as file:
    #     for x in very_hard_list:
    #         file.write(str(x[0]) + ": " + str(x[1]) + "\n")
            

    score = (correct/counter)*100
    print('')
    return 'your final score is '+ str(score) + ' %'




def hsk2_quiz():
    hsk2_words = ['吧', '白', '百', '帮助', '报纸', '比', '别', '宾馆', '长', '唱歌', 
                '出', '穿', '次', '从', '错', '打篮球', '大家', '到', '得', '等', 
                '弟弟', '第一', '懂', '对', '对', '房间', '非常', '服务员', '高', 
                '告诉', '哥哥', '给', '公共汽车', '公司', '贵', '过', '孩子', '还', 
                '好吃', '黑', '红', '火车站', '机场', '鸡蛋', '件', '教室', '姐姐', 
                '介绍', '近', '进', '就', '觉得', '咖啡', '开始', '考试', '可能', 
                '可以', '课', '快', '快乐', '累', '离', '两', '零', '路', '旅游', 
                '卖', '慢', '忙', '每', '妹妹', '门', '面条', '男', '您', '牛奶', 
                '女', '旁边', '跑步', '便宜', '票', '妻子', '起床', '千', '铅笔', 
                '晴', '去年', '让', '日', '上班', '身体', '生病', '生日', '时间', 
                '事情', '手表', '手机', '说话', '送', '虽然…但是…', '它', '踢足球', 
                '题', '跳舞', '外', '完', '玩', '晚上', '往', '为什么', '问', '问题', 
                '希望', '西瓜', '洗', '小时', '笑', '新', '姓', '休息', '雪', '颜色', 
                '眼睛', '羊肉', '药', '要', '也', '一下', '已经', '一起', '意思', '因为…所以…', 
                '阴', '游泳', '右边', '鱼', '远', '运动', '再', '早上', '丈夫', '找', 
                '着', '真', '正在', '知道', '准备', '走', '最', '左边']



    hsk2_pinyin = []

    for hanzi in hsk2_words:
        pinyin_word = ' '.join([s[0] for s in pinyin(hanzi, style=Style.TONE)])
        hsk2_pinyin.append(pinyin_word)

    hsk2_normalized_pinyin = [remove_accents(word) for word in hsk2_pinyin]

    hsk2_hanzi_pinyin_dict = dict(zip(hsk2_words, hsk2_pinyin))

    normalize_hsk2_hanzi_pinyin_dict = dict(zip(hsk2_words, hsk2_normalized_pinyin))

    hsk2_key_list = list(hsk2_hanzi_pinyin_dict.keys())
    hsk2_value_list = list(hsk2_hanzi_pinyin_dict.values())

    correct= 0
    incorrect = []


    counter = 0

    c = len(hsk2_key_list) # change c to choose the number of characters to study....to study all, change c to len(key_list)


    random_key_list = random.sample(hsk2_key_list, len(hsk2_value_list))

    # for x in random.sample(key_list, len(key_list)): #uncomment this line if you want to study all of the characters
    for x in random_key_list[:c]: 
        counter+=1
        answer=input('Hanzi: '+ str(x)+ ' Pinyin: ')
        print('')
        if answer == normalize_hsk2_hanzi_pinyin_dict[x]:
            print(hsk2_hanzi_pinyin_dict[x]+ ' is correct')
            print('')
            correct+=1
        else:
            print('')
            print('That is incorrect. The answer is ' + hsk2_hanzi_pinyin_dict[x])
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
        score = (correct/len(hsk2_words))*100
        print('')
        print('your final score is '+ str(score) + ' %') 
    else:
        for x in random.sample(incorrect, len(incorrect)):
            counter +=1
            answer=input('Hanzi: '+ str(x)+ ' Pinyin: ')
            if answer == normalize_hsk2_hanzi_pinyin_dict[x]:
                print('')
                print(hsk2_hanzi_pinyin_dict[x]+ ' is correct')
                correct+=1
            else:
                print('')
                print('That is incorrect. The answer is ' + hsk2_hanzi_pinyin_dict[x])
                very_hard_dict[x]= hsk2_hanzi_pinyin_dict[x]

    print("")
    print("")
    print('Need to study the following:')
    print("")
    print(very_hard_dict)

    very_hard_list = []

    for x in very_hard_dict:
        very_hard_list.append([x, very_hard_dict[x]])



    # with open("practice.txt", "w", encoding= "utf-8") as file:
    #     for x in very_hard_list:
    #         file.write(str(x[0]) + ": " + str(x[1]) + "\n")
            

    score = (correct/counter)*100
    print('')
    return 'your final score is '+ str(score) + ' %'




def level_select():
    level = 0
    while level == 0:
        hsk_level = input("which HSK level do you want to practice? Type 1 or 2: ")
        if hsk_level == '1':
            print(hsk1_quiz())
            level = 1
        elif hsk_level == '2':
            print(hsk2_quiz())
            level = 2
        else:
            level = 0
print(level_select())



while again == 0:
    another_practice = input('Do you want to continue practicing? Type yes or no: ')
    if another_practice == 'yes':
        again_level = 0
        while again_level == 0:
            which_level = input('Which level do you want to practice? Type 1 or 2: ')
            if which_level == '1':
                print(hsk1_quiz())
                again_level = 1
            elif which_level == '2':
                print(hsk2_quiz())
                
    elif another_practice == 'no':
        break
    else:
        again = 0

    





