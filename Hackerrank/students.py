if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    score = lambda item : (item[1], item[0])
    by_score = sorted(students, key=score)

    score_2nd = by_score[0][1]
    for x in range(1,len(by_score)):
        if (by_score[x][1] > score_2nd):
            score_2nd = by_score[x][1]
            break
    
    for student in by_score:
        if (student[1] == score_2nd):
            print(student[0])
