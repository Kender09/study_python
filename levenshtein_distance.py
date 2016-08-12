import Levenshtein
import MeCab

mecab = MeCab.Tagger('/usr/local/lib/mecab/dic/mecab-ipadic-neologd')
arr = []

for line in open('raw_romaji.tsv', 'r'):
    set = line[:-1].split('\t')
    text = set[0]
    mecab.parse('')
    node = mecab.parseToNode(text)
    use_flag = 0
    while node:
        word = node.surface
        pos = node.feature.split(",")[0]
        if pos == '名詞' and word == text:
            use_flag = 1
            break
        if (pos == '動詞' or pos == '助詞') and word == text:
            use_flag = 2
            break
        node = node.next
    set.append(use_flag)
    arr.append(set)

for i in range(len(arr)):
    if not arr[i][2] == 1 : continue
    score_d = {}
    for n in range(len(arr) - (i + 1)):
        if arr[n + i + 1][2] == 2: continue
        score = Levenshtein.distance(arr[i][1], arr[n + i + 1][1])
        score_d[n + i + 1] = float(score) / len(arr[i][1])
    ans_str = ''
    for k, v in sorted(score_d.items(), key=lambda x: x[1]):
        if v > 0.2: break
        ans_str += ',' + arr[k][0]
    if ans_str: print(arr[i][0] + ans_str)

