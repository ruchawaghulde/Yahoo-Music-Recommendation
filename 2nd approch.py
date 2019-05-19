from __future__ import print_function
import time
import sys


dataDir = '/Users/siddharthmandgi/Desktop/data_in_matrixForm/'
OUTPUT_FILE = dataDir + 'output2.txt'
H_FILE = dataDir + 'testTrack_hierarchy.txt'
TRAIN_FILE = dataDir + 'trainItem2.txt'

user_rate = {}
start_time = time.time()
with open(TRAIN_FILE) as train:
    for line in train:
        if "|" in line:
            cur_user = line.strip("\n").split("|")[0]
            user_rate[cur_user] = {}
            continue
        item_id, item_score = line.strip("\n").split()
        user_rate[cur_user][item_id] = item_score

with open(OUTPUT_FILE, "w") as output:
    with open(H_FILE) as record:
        for line in record:
            gen_out = ""
            user, track = line.strip("\n").split("|")[0], line.strip("\n").split("|")[1]
            items = line.strip("\n").split("|")[2:]
            if len(items) == 0:
                album_score = 'None'
                artist_score = 'None'
            if len(items) == 1:
                album = items[0]
                try:
                    album_score = user_rate[user][album]
                except KeyError:
                    album_score = 'None'
                artist_score = 'None'
            if len(items) == 2:
                album = items[0]
                artist = items[1]
                try:
                    album_score = user_rate[user][album]
                except KeyError:
                    album_score = 'None'
                try:
                    artist_score = user_rate[user][artist]
                except KeyError:
                    artist_score = 'None'
            if len(items) > 2:
                try:
                    album_score = user_rate[user][items[0]]
                except KeyError:
                    album_score = 'None'
                try:
                    artist_score = user_rate[user][items[1]]
                except KeyError:
                    artist_score = 'None'
                genr = items[2:]
                for g in genr:
                    try:
                        gen_out = gen_out + "|" + user_rate[user][g]
                    except KeyError:
                        pass
            output.write(user + "|" + track + "|" + album_score + "|" + artist_score + gen_out + "\n")

print("Finished, Spend %.2f s" % (time.time() - start_time))

output_file = dataDir + 'output2.txt'
submission_file = dataDir + 'submission5.txt'

fResult = open(output_file, 'r')
fSubmission = open(submission_file, 'w')

res = str('TrackID') + ',' + str('Predictor')
fSubmission.write(res + '\n')

for rline in fResult:
    score = 0
    arr_test = rline.strip().split('|')
    ruserID = arr_test[0]
    rtrackID = arr_test[1]

    if len(arr_test) == 3:
        Rating_1 = arr_test[2]
        if Rating_1 == '1':
            score = 1

    if len(arr_test) == 4:
        Rating_1 = arr_test[2]
        Rating_2 = arr_test[3]
        if Rating_1 == '1' and Rating_2 == '1':
            score = 1
        elif Rating_1 == '1' or Rating_2 == '1':
            score = 1



    elif len(arr_test) == 5:
        Rating_1 = arr_test[2]
        Rating_2 = arr_test[3]
        Rating_3 = arr_test[4]
        if Rating_1 == '1' and Rating_2 == '1':
            score = 1

        elif Rating_1 == '1' or Rating_2 == '1':
            score = 1


        elif Rating_1 != '1' and Rating_2 != '1':
            if Rating_3 != 'None':
                score = 1





    elif len(arr_test) == 6:
        Rating_1 = arr_test[2]
        Rating_2 = arr_test[3]
        Rating_3 = arr_test[4]
        Rating_4 = arr_test[5]
        if Rating_1 == '1' and Rating_2 == '1':
            score = 1

        elif Rating_1 == '1' or Rating_2 == '1':
            score = 1

        elif Rating_1 != '1' and Rating_2 != '1':
            if Rating_3 != 'None' and Rating_4 != 'None':
                score = 1

        else:
            score = 0



    elif len(arr_test) == 7:
        Rating_1 = arr_test[2]
        Rating_2 = arr_test[3]
        Rating_3 = arr_test[4]
        Rating_4 = arr_test[5]
        Rating_5 = arr_test[6]
        if Rating_1 == '1' and Rating_2 == '1':
            score = 1

        elif Rating_1 == '1' or Rating_2 == '1':
            score = 1

        elif Rating_1 != '1' and Rating_2 != '1':
            if Rating_3 != 'None' and Rating_4 != 'None' and Rating_5 != 'None':
                score = 1

    res = str(ruserID) + '_' + str(rtrackID) + ',' + str(score)
    fSubmission.write(res + '\n')

fSubmission.close()
fResult.close()

