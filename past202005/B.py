N,M,Q = map(int,input().split())
participant,problem_score = [0]*N,[0]*M
problem_participant = [[0]*N for i in range(M)]
change_list = [0] * M
all_score = []
first = 0
# print(problem_participant)
tmp = []
for i1 in range(Q):
    x = list(map(int,input().split()))
    if x[0] == 1:
        tmp_score = 0
        if first == 0:
            for i2 in problem_participant:
                score = N - sum(i2)
                all_score.append([score,i2])

        for index2,i1 in enumerate(change_list):
            if i1 == 1:
                for index1,i2 in enumerate(problem_participant):
                    if i2[x[1] - 1] == 1:
                        score = N-sum(i2)
                        tmp_score = tmp_score + score
                        all_score[index1] = [score,i2]
                        change_list[index2] = 0
            else:
                if all_score[index2][1][x[1] -1] == 1:
                    tmp_score = tmp_score + all_score[index2][0]
        else:
            tmp.append(tmp_score)
    else:
        problem_participant[x[2]-1][x[1]-1] = 1
        change_list[x[2]-1] = 1
        # print(problem_participant)

[print(i) for i in tmp]

#もし１なら計算を行う
    #もし初めての計算処理ならすべての計算を行う
        #all_scoreリストを作る
    #もし変更されていたら計算処理を行う
        #スコアを算出する
        #tmp_scoreに足す
        #all_scoreリストを更新する
        #change_listを初期化する
    #変更されていなければ過去の記録を使う
        #all_scoreリストの点数をtmp_scoreに足す
    #すべてが終了した時点でtmpリストにtmp_scoreを足す
#もし２なら入力処理を行う
    #problem_pariticipantリストの該当箇所に１を追加する
    #変更された位置をchange_listに追加する