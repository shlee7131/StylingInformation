import json

with open('C:/Users/homeg/Desktop/SSF.json', encoding = 'utf-8') as f:
    ssf = json.load(f)

with open('C:/Users/homeg/Desktop/Musinsa.json', encoding = 'utf-8') as f:
    musinsa = json.load(f)

with open('C:/Users/homeg/Desktop/new_tags.json', encoding = 'utf-8') as f:
    tags = json.load(f)

with open('C:/Users/homeg/Desktop/relations_50.json', encoding = 'utf-8') as f:
    ssf_recommend = json.load(f)

with open('C:/Users/homeg/Desktop/ssf_wear.json', encoding = 'utf-8') as f:
    ssf_wear = json.load(f)

with open('C:/Users/homeg/Desktop/musinsa_wear.json', encoding = 'utf-8') as f:
    musinsa_wear = json.load(f)


ssf_tshirts = []
ssf_pants = []
ssf_skirts = []
ssf_others = []
for i in ssf:
    if i['superCategory'] == "상의" and i not in ssf_tshirts:
        ssf_tshirts.append(i)
    elif i['superCategory'] == "팬츠" and i not in ssf_pants:
        ssf_pants.append(i)
    elif i['superCategory'] == "스커트" and i not in ssf_skirts:
        ssf_skirts.append(i)
    elif i not in ssf_others:
        ssf_others.append(i)


musinsa_tshirts = []
musinsa_pants = []
musinsa_skirts = []
musinsa_others = []
for i in musinsa:
    if i['superCategory'] == "상의" and i not in musinsa_tshirts:
        musinsa_tshirts.append(i)
    elif i['superCategory'] == "바지" and i not in musinsa_pants:
        i['superCategory'] == "팬츠"
        musinsa_pants.append(i)
    elif i['superCategory'] == "스커트" and i not in musinsa_skirts:
        musinsa_skirts.append(i)
    elif i not in musinsa_others:
        musinsa_others.append(i)


tshirts_cat_set = set()
pants_cat_set = set()
for i in ssf_tshirts:
    tshirts_cat_set.add((i['midCategory'],i['category']))
for i in ssf_pants:
    pants_cat_set.add((i['midCategory'],i['category']))

#print(tshirts_cat_set)

# ssf 상의 카테고리 변경
for i in ssf_tshirts:
    if i['midCategory'] == '민소매':
        pass
    elif i['category'] == '카라 티셔츠':
        temp = i['midCategory']
        i['midCategory'] = '피케/카라 티셔츠'
        i['category'] = temp
    elif i['category'] == '맨투맨/스웨트 셔츠':
        temp = i['midCategory']
        i['midCategory'] = '맨투맨/스웨트셔츠'
        i['category'] = temp
    elif i['category'] == "후드 티셔츠":
        temp = i['midCategory']
        i['midCategory'] = '후드 티셔츠'
        i['category'] = temp
    elif i['midCategory'] == '반팔':
        i['midCategory'] = '반팔 티셔츠'
    elif i['midCategory'] == '긴팔':
        i['midCategory'] = '긴팔 티셔츠'

# ssf 팬츠 카테고리 변경
for i in ssf_pants:
    if i['midCategory'] == '쇼츠':
        i['midCategory'] = '숏 팬츠'
    elif i['midCategory'] == '데님':
        i['midCategory'] = '데님 팬츠'
    elif i['midCategory'] == '캐주얼' and i['material'] == "면":
        i['midCategory'] = '코튼 팬츠'
    elif i['midCategory'] == '캐주얼' and i['category'] == "레깅스":
        i['midCategory'] = '레깅스'
        i['category'] == None
    elif i['midCategory'] == "포멀":
        i['midCategory'] = "슈트 팬츠/슬랙스"
    elif i['midCategory'] == "스포츠":
        i['midCategory'] = "트레이닝/조거 팬츠"
    elif i['midCategory'] == "점프수트":
        i['midCategory'] = "점프 슈트/오버올"
    else:
        i['midCategory'] = "기타 바지"


    if i['category'] == "쇼트 팬츠":
        i['category'] = "숏 팬츠"

    if i['category'] == "숏 팬츠":
        temp = i['midCategory']
        i['midCategory'] = "숏 팬츠"
        i['category'] = temp

    if i['category'] == "롱팬츠":
        i['category'] = "롱 팬츠"

        # elif i['category'] == "쇼트 팬츠":
    #     temp = i['midCategory']
    #     i['midCategory'] == "숏 팬츠"
    #     i['category'] = temp



# tshirts_cat_set = set()
pants_cat_set = set()
for i in ssf_tshirts:
    tshirts_cat_set.add((i['midCategory'],i['category']))
for i in ssf_pants:
    # pants_cat_set.add((i['midCategory'],i['category']))
    pants_cat_set.add((i['midCategory']))

# print(tshirts_cat_set)
print(pants_cat_set)

tshirts_cat_set = set()
pants_cat_set = set()
for i in musinsa_tshirts:
    tshirts_cat_set.add((i['midCategory'],i['category']))
for i in musinsa_pants:
    # pants_cat_set.add((i['midCategory'],i['category']))
    pants_cat_set.add((i['midCategory']))

# print(tshirts_cat_set)
print(pants_cat_set)

ssf_new = ssf_tshirts + ssf_pants + ssf_skirts + ssf_others
musinsa_new = musinsa_tshirts + musinsa_pants + musinsa_skirts + musinsa_others

for i in musinsa_new:
    if i['superCategory'] == '바지':
        i['superCategory'] = '팬츠'

# 무신사 패턴 칼럼 추가
for i in musinsa_new:
    i['pattern'] = None

# SSF 테이블 구조 변경
for i in ssf_new:
    del i['coordination']
    i['mall'] = "SSF"
    i['product_img'] = i['img_src']
    del i['img_src']
    i['tag'] = i['fit']
    #del i['fit']
    i['fit']
    try:
        i['tag'] += "," + i['style']
    except TypeError as e:
        pass
    #del i['style']
    del i['wearing_id']
    del i['wearing_img']
    i['is_wear'] = "0"
    i['is_recommend'] = "0"

# 무신사 태그에서 핏 정보 가져오기
def fit_in_tag(hashtag_string):
    res = None
    if '오버핏' in hashtag_string or '오버사이즈' in hashtag_string:
        res = '오버핏'
    if '레귤러' in hashtag_string:
        res = '레귤러핏'
    if '루즈' in hashtag_string:
        res = '루즈핏'
    if '슬림' in hashtag_string:
        res = '슬림핏'
    if '스트레이트핏' in hashtag_string:
        res = '슬림/스트레이트'
    if '와이드팬츠' in hashtag_string:
        res = '와이드'
    if '조거' in hashtag_string:
        res = '조거'

    return res

# 무신사 태그에서 스타일 정보 가져오기
def style_in_tag(hashtag_string):
    res = ''
    if '캐주얼' in hashtag_string or '데일리' in hashtag_string or '베이직' in hashtag_string:
        res += '캐주얼,'
    if '모던' in hashtag_string or '미니멀' in hashtag_string:
        res += '모던/미니멀,'
    if '스트릿' in hashtag_string:
        res += '스트릿,'
    if '페미닌' in hashtag_string:
        res += '페미닌,'
    if '클래식' in hashtag_string:
        res += '클래식/프레피,'
    if '스포츠' in hashtag_string:
        res += '액티브/스포티,'
    return res[:-1]


# Musinsa 테이블 구조 변경
for i in musinsa_new:
    i["mall"] = "Musinsa"
    i['tag'] = ""
    i['fit'] = None
    for j in tags:
        if i['product_id'] == j['product_id']:
            if j['tags'] != "":
                i['tag'] = j['tags']
    if i['계절']:
        season = i['계절']
        i['tag'] += "," + season
    if i['비침']:
        transparency = i['비침']
        i['tag'] += "," + "비침 " + transparency
    if i['신축성']:
        flexibility = i['신축성']
        i['tag'] += "," + "신축성 " + flexibility
    if i['두께']:
        thickness = i['두께']
        i['tag'] += "," + "두께 " + thickness
    if i['촉감']:
        touch = i['촉감']
        i['tag'] += "," + "촉감 " + touch
    if i['핏']:
        fit = i['핏']
        i['tag'] += "," + touch
    del i['핏']
    del i['계절']
    del i['신축성']
    del i['두께']
    del i['촉감']
    del i['비침']
    if i['tag'] == "":
        i['tag'] = None
    try:
        i['price'] = i['price'].strip()
    except AttributeError as e:
        pass
    i['is_wear'] = "1"
    i['is_recommend'] = "0"
    del i['codi_num']
    # 스타일 칼럼 생성
    i['style'] = None
    try:
        i['style'] = style_in_tag(i['tag'])
        i['fit'] = fit_in_tag(i['tag'])
    except TypeError as e:
        pass


def color_change(ann_list):
    for i in ann_list:
        i['color_detail'] = None
        try:
            if "회색" in i['color']:
                i['color_detail'] = i['color']
                i['color'] = "회색"
            elif i['color'] in ["녹색", "애플그린", "올리브", "연두색"]:
                i['color_detail'] = i['color']
                i['color'] = "초록색"
            elif i['color'] in ["노란색", "겨자색", "노란색(골드)", "레몬"]:
                i['color_detail'] = i['color']
                i['color'] = "노란색"
            elif "분홍" in i['color']:
                i['color_detail'] = i['color']
                i['color'] = "핑크색"
            elif i['color'] in ["주황색(브론즈)","코럴"]:
                i['color_detail'] = i['color']
                i['color'] = "주황색"
            elif i['color'] in ["하늘색", "남색", "로열 블루"]:
                i['color_detail'] = i['color']
                i['color'] = "파란색"
            elif "갈색" in i['color'] or '카키' in i['color']:
                i['color_detail'] = i['color']
                i['color'] = "갈색"
            elif "라벤다" in i['color']:
                i['color_detail'] = i['color']
                i['color'] = "보라색"
            elif "와인" in i['color']:
                i['color_detail'] = i['color']
                i['color'] = "빨간색"
            elif i['color'] in ["흰색", "아이보리"]:
                i['color_detail'] = i['color']
                i['color'] = "흰색"
            elif "베이지" in i['color'] or "카멜" in i['color']:
                i['color_detail'] = i['color']
                i['color'] = "베이지"
        except TypeError as e:
            pass

color_change(ssf_new)
color_change(musinsa_new)

wear_dict = {
    'product_id' : None,
    'category' : None,
    'style' : None,
    "codi_num" : None,
    "url" : None,
    "model_img" : None,
    "mall" : None,
    "product_img" : None
}

# SSF 착장 정보
ssf_codi_num = []
wear_temp_list = []
for i in ssf_wear:
    i["mall"] = "SSF"

    if i['product_id'] not in ssf_codi_num:
        ssf_codi_num.append(i['product_id'])
    i['codi_num'] = str(ssf_codi_num.index(i['product_id']) + 1)

    i['combination_img'] = i['img_src']
    i['product_img'] = None
    for j in ssf_new:
        if i['product_id'] == j['product_id']:
            i['product_img'] = j['product_img']
            j['is_wear'] = "1"
    del i['img_src']
    del i['combination_brand']
    i['url'] = None
    i['style'] = None
    wear_temp = wear_dict.copy()
    wear_temp['product_id'] = i['combination_id']
    del i['combination_id']
    wear_temp['category'] = i['category']
    i['category'] = "상의"
    wear_temp['codi_num'] = i['codi_num']
    wear_temp['model_img'] = i['model_img']
    wear_temp['product_img'] = i['combination_img']
    wear_temp['mall'] = "SSF"
    del i['combination_img']
    wear_temp_list.append(wear_temp)

# ssf_wear 테이블 분할
ssf_wear += wear_temp_list
# ssf_wear 중복 제거
redundancy = []
ssf_temp = []
for i in ssf_wear:
    temp = (i['product_id'],i['codi_num'])
    if temp not in redundancy:
        redundancy.append(temp)
        ssf_temp.append(i)

ssf_wear = ssf_temp


# Musinsa 착장 정보
for i in musinsa_wear:
    i["mall"] = "Musinsa"
    for j in musinsa_new:
        if i['product_id'] == j['product_id']:
            i['product_img'] = j['product_img']
            break
    del i['brand_name']
    del i['brand_id']
    del i['sex']
    if i['category'] == '바지':
        i['category'] = '팬츠'


# 매칭 색상 정보
for i in ssf_wear:
    i['upper_color'] = None
    i['bottom_color'] = None
    codi_num = i['codi_num']
    if i['category'] == "상의":
        for j in ssf_new:
            if j['product_id'] == i['product_id']:
                color = j['color']
                i['upper_color'] = color
        for h in ssf_wear:
            if h['codi_num'] == codi_num and (h['category'] == "팬츠" or h['category'] == "스커트"):
                wear_id = h['product_id']
                if i['bottom_color'] is None:
                    for j in ssf_new:
                        if j['product_id'] == wear_id:
                            color = j['color']
                            i['bottom_color'] = color
    elif i['category'] == "팬츠" or i['category'] == "스커트":
        for j in ssf_new:
            if j['product_id'] == i['product_id']:
                color = j['color']
                i['bottom_color'] = color
        for h in ssf_wear:
            if h['codi_num'] == codi_num and (h['category'] == "상의"):
                wear_id = h['product_id']
                if i['upper_color'] is None:
                    for j in ssf_new:
                        if j['product_id'] == wear_id:
                            color = j['color']
                            i['upper_color'] = color


for i in musinsa_wear:
    i['upper_color'] = None
    i['bottom_color'] = None
    if i['category'] == "상의":
        for j in musinsa_new:
            if j['product_id'] == i['product_id']:
                color = j['color']
                i['upper_color'] = color
        for h in musinsa_wear:
            if h['codi_num'] == i['codi_num']:
                if (h['category'] == "팬츠" or h['category'] == "스커트"):
                    wear_id = h['product_id']
                    if i['bottom_color'] is None:
                        for k in musinsa_new:
                            if k['product_id'] == wear_id:
                                color = k['color']
                                i['bottom_color'] = color
    elif i['category'] == "팬츠" or i['category'] == "스커트":
        for j in musinsa_new:
            if j['product_id'] == i['product_id']:
                color = j['color']
                i['bottom_color'] = color
        for h in musinsa_wear:
            if h['codi_num'] == i['codi_num']:
                if h['category'] == "상의":
                    wear_id = h['product_id']
                    if i['upper_color'] is None:
                        for k in musinsa_new:
                            if k['product_id'] == wear_id:
                                color = k['color']
                                i['upper_color'] = color


# ssf 추천 정보
for i in ssf_recommend:
    i['product_category'] = None
    for j in ssf_tshirts:
        if i['product_id'] == j['product_id']:
            i['product_category'] = "상의"
    recommend_id = i['recommend_id']
    i['recommend_category'] = i['category']
    for h in ssf_new:
        if recommend_id == h['product_id']:
            ssf_recommend_cat = h['superCategory']
            i['recommend_category'] = ssf_recommend_cat
            break
    i['recommend_number']= str(i['coordination_number'])
    i['mall'] = "SSF"
    del i['coordination_number']
    del i['category']

    for h in ssf_new:
        if i['product_id'] == h['product_id']:
            h['is_recommend'] = "1"

musinsa_recommend = []
recommend = {
    "product_id" : None,
    "recommend_id" : None,
    "product_category" : None,
    "recommend_category" : None,
    "recommend_number" : 0,
    "mall" : None
}
count = 0

# musinsa 추천 정보
# for i in musinsa_new:
#     recommend_temp = recommend.copy()
#     for j in musinsa_wear:
#         if i['product_id'] == j['product_id']:
#             recommend_temp['product_id'] = j['product_id']
#             recommend_temp['product_category'] = j['category']
#             if recommend_temp['product_category'] == "바지" or recommend_temp['product_category'] == "스커트":
#                 recommend_temp['recommend_category'] == "하의"
#             for h in musinsa_wear:
#                 if j['codi_num'] == h['codi_num'] and j['product_id'] != h['product_id']:
#                     recommend_temp['recommend_id'] = h['product_id']
#                     recommend_temp['recommend_category'] = h['category']
#                     if recommend_temp['recommend_category'] == "바지" or recommend_temp['recommend_category'] == "스커트":
#                         recommend_temp['recommend_category'] == "하의"
#             recommend_temp['mall'] = "Musinsa"
#             recommend_temp['recommend_number'] = "1" # 수정 필요
#
#     musinsa_recommend.append(recommend_temp)

count = 1
for i in musinsa_new:
    recommend_temp = recommend.copy()
    count = 1
    for j in musinsa_wear:
        if i['product_id'] == j['product_id'] and i['superCategory'] == "상의":
            recommend_temp['product_id'] = j['product_id']
            recommend_temp['product_category'] = "상의"
            for h in musinsa_wear:
                if j['codi_num'] == h['codi_num'] and h['product_id'] != j['product_id']:
                    recommend_temp_temp = recommend_temp.copy()
                    recommend_temp_temp['recommend_id'] = h['product_id']
                    recommend_temp_temp['recommend_category'] = h['category']
                    recommend_temp_temp['mall'] = "Musinsa"
                    recommend_temp_temp['recommend_number'] = str(count)
                    musinsa_recommend.append(recommend_temp_temp)
            count += 1

# 중복제거
redundancy = []
musinsa_recommend_temp = []
for i in musinsa_recommend:
    if [i['product_id'],i['recommend_id']]not in redundancy:
        musinsa_recommend_temp.append(i)
        redundancy.append([i['product_id'],i['recommend_id']])
musinsa_recommend = musinsa_recommend_temp



# 무신사 추천 여부
for i in musinsa_new:
    for j in musinsa_recommend:
        if i['product_id'] == j['product_id']:
            i['is_recommend'] = "1"

# 패턴 작업 _ 무신사
for i in musinsa_new:
    i['pattern_detail'] = None
    product_name = i['product_id']
    tag_info = i['tag']
    if product_name is not None:
        if '스트라이프' in product_name:
            i['pattern'] = '스트라이프'
        elif '도트' in product_name:
            i['pattern'] = '도트'
        elif '체크' in product_name:
            i['pattern'] = '체크'
        elif '플라워' in product_name:
            i['pattern'] = '플라워'
        elif '카모' in product_name:
            i['pattern'] = '카모'
        elif '애니멀' in product_name:
            i['pattern'] = '애니멀'
        elif '그래픽' in product_name:
            i['pattern'] = '그래픽'
        elif '페이즐리' in product_name:
            i['pattern'] = '페이즐리'
        elif '패치워크' in product_name:
            i['pattern'] = '패치워크'
        elif '트로피컬' in product_name:
            i['pattern'] = '트로피컬'
        elif '그라데이션' in product_name:
            i['pattern'] = '그라데이션'
        elif '타이포그래피' in product_name:
            i['pattern'] = '타이포그래피'
    if tag_info is not None and i['pattern'] is None:
        if '스트라이프' in tag_info:
            i['pattern'] = '스트라이프'
        elif '도트' in tag_info:
            i['pattern'] = '도트'
        elif '체크' in tag_info:
            i['pattern'] = '체크'
        elif '플라워' in tag_info:
            i['pattern'] = '플라워'
        elif '카모' in tag_info:
            i['pattern'] = '카모'
        elif '애니멀' in tag_info:
            i['pattern'] = '애니멀'
        elif '그래픽' in tag_info:
            i['pattern'] = '그래픽'
        elif '페이즐리' in tag_info:
            i['pattern'] = '페이즐리'
        elif '패치워크' in tag_info:
            i['pattern'] = '패치워크'
        elif '트로피컬' in tag_info:
            i['pattern'] = '트로피컬'
        elif '그라데이션' in tag_info:
            i['pattern'] = '그라데이션'
        elif '타이포그래피' in tag_info:
            i['pattern'] = '타이포그래피'
        elif '기타' in tag_info:
            i['pattern'] = '기타'
        else:
            i['pattern'] = '솔리드'

# 패턴 작업 _ SSF
for i in ssf_new:
    pattern = i['pattern']
    i['pattern_detail'] = None
    if pattern is None:
        pass
    elif pattern == "가로 스트라이프":
        i['pattern_detail'] = pattern
        i['pattern'] = '스트라이프'
    elif pattern == "도트":
        i['pattern_detail'] = pattern
        i['pattern'] = '도트'
    elif pattern in ["아가일", "깅업", "타탄"]:
        i['pattern_detail'] = pattern
        i['pattern'] = '체크'
    elif pattern in ["플로럴"]:
        i['pattern_detail'] = pattern
        i['pattern'] = '플라워'
    elif pattern in ["카모플라쥬"]:
        i['pattern_detail'] = pattern
        i['pattern'] = '카모'
    elif pattern in ["카모플라쥬"]:
        i['pattern_detail'] = pattern
        i['pattern'] = '카모'
    elif pattern in ["그라데이션"]:
        i['pattern_detail'] = pattern
        i['pattern'] = '그라데이션'
    elif pattern in ["애니멀"]:
        i['pattern_detail'] = pattern
        i['pattern'] = '애니멀'
    elif pattern in ["트로피컬"]:
        i['pattern_detail'] = pattern
        i['pattern'] = '트로피컬'
    elif pattern in ["타이포그래피"]:
        i['pattern_detail'] = pattern
        i['pattern'] = '타이포그래피'
    elif pattern in ["그래픽"]:
        i['pattern_detail'] = pattern
        i['pattern'] = '그래픽'
    elif pattern in ["기타"]:
        i['pattern_detail'] = pattern
        i['pattern'] = '기타'
    else:
        i['pattern_detail'] = pattern
        i['pattern'] = '기타'



with open('C:/Users/homeg/Desktop/SSF_new.json', 'w', encoding = 'utf-8') as f:
    json.dump(ssf_new, f, ensure_ascii= False, indent = '\t')

with open('C:/Users/homeg/Desktop/Musinsa_new.json', 'w', encoding = 'utf-8') as f:
    json.dump(musinsa_new, f, ensure_ascii= False, indent = '\t')

with open('C:/Users/homeg/Desktop/ssf_recommend.json', 'w', encoding = 'utf-8') as f:
    json.dump(ssf_recommend, f, ensure_ascii= False, indent = '\t')

with open('C:/Users/homeg/Desktop/ssf_wear_new.json', 'w', encoding = 'utf-8') as f:
    json.dump(ssf_wear, f, ensure_ascii= False, indent = '\t')

with open('C:/Users/homeg/Desktop/musinsa_wear_new.json', 'w', encoding = 'utf-8') as f:
    json.dump(musinsa_wear, f, ensure_ascii= False, indent = '\t')

with open('C:/Users/homeg/Desktop/musinsa_recommend.json', 'w', encoding = 'utf-8') as f:
    json.dump(musinsa_recommend, f, ensure_ascii= False, indent = '\t')

recommend = ssf_recommend + musinsa_recommend
information = ssf_new + musinsa_new
wear = ssf_wear + musinsa_wear




with open('C:/Users/homeg/Desktop/recommend.json', 'w', encoding = 'utf-8') as f:
    json.dump(recommend, f, ensure_ascii= False, indent = '\t')
with open('C:/Users/homeg/Desktop/information.json', 'w', encoding = 'utf-8') as f:
    json.dump(information, f, ensure_ascii= False, indent = '\t')
with open('C:/Users/homeg/Desktop/wear.json', 'w', encoding = 'utf-8') as f:
    json.dump(wear, f, ensure_ascii= False, indent = '\t')

