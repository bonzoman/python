# 파일 리스트
filenames = ['./DataFiles/sampleTxt1.txt', './DataFiles/sampleTxt2.txt']

with open('./DataFiles/sampleTxt_All.txt', 'w', encoding='utf-8') as outfile:
    for filename in filenames:
        with open(filename, 'rt', encoding='UTF8') as file:
            # case 1
            for line in file:
                outfile.write(line)

            # case 2
            # outfile.write(file.read())
