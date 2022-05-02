import re
#
# text=str(b"Cloning into 'awesome-python'...\n")
# m=re.search('Cloning into \'(.+)\'.*', text)
# if m:
#     print(m.group(1))


log='''[c3c098dcf] Remita Amine 2018-12-07 [hotstar] fix video data extraction(closes #18386)
2       1       youtube_dl/extractor/hotstar.py

[adbbdefc8] Sergey M․ 2018-11-30 [hotstar] Add support for alternative app state layout (closes #18320)
10      1       youtube_dl/extractor/hotstar.py

[05e7c184d] Remita Amine 2018-10-02 [hotstar] fix extraction in python 2(closes #17696)
6       1       youtube_dl/extractor/hotstar.py

[85cd69adc] Remita Amine 2018-09-26 [hotstar] fix extraction(closes #14694)(closes #14931)(closes #17637)
75      88      youtube_dl/extractor/hotstar.py

[909191de9] Sergey M․ 2017-11-05 [hotstar:playlist] Fix issues and improve (closes #12465)
62      58      youtube_dl/extractor/hotstar.py

[477c97f86] Alpesh Valia 2017-03-16 [hotstar:playlist] Add extractor
57      1       youtube_dl/extractor/hotstar.py

[6e71bbf4a] Sergey M․ 2017-11-05 [hotstar] Bypass geo restriction (closes #14672)
1       0       youtube_dl/extractor/hotstar.py

[0dac7cbb0] Remita Amine 2017-02-12 [hotstar] improve extraction(closes #12096)
32      14      youtube_dl/extractor/hotstar.py

[89d23f37f] Sergey M․ 2016-02-10 [hotstar] Relax _VALID_URL (Closes #8487)
9       3       youtube_dl/extractor/hotstar.py

[7e5edcfd3] Sergey M․ 2015-12-29 Simplify formats accumulation for f4m/m3u8/smil formats
1       3       youtube_dl/extractor/hotstar.py

[fb8e402ad] remitamine 2015-12-25 [hotstar] Add new extractor
79      0       youtube_dl/extractor/hotstar.py
'''

'''format: [fb8e402ad] remitamine@gmail.com 2015-12-25 [hotstar] Add new extractor'''
line1_pattern=r'^\[([0-9abcdef]+)\](.*) ([0-9]{4}-[0-9]{2}-[0-9]{2}) (.*)$'

'''format: 79      0       youtube_dl/extractor/hotstar.py'''
line2_pattern=r'^([0-9]+)\s*([0-9]+)\s*.*$'


log_parsed = log.split('\n\n')
print(log_parsed)
for commit in log_parsed:
    lines = commit.split('\n')
    m_line1 = re.search(line1_pattern, lines[0])
    m_line2 = re.search(line2_pattern, lines[1])

    author, date, message = m_line1.group(2), m_line1.group(3), m_line1.group(4)
    lines_added, lines_deleted = m_line2.group(1), m_line2.group(2)

    print('ok')




