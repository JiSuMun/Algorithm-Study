# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

# O(N*M) N:문제의 수, M:수포자의 수
def solution(answers):
    answer = []
    # scores : 각 수포자들의 점수가 담긴 배열
    scores = []
    # estimates : 각 수포자들의 찍기 조합
    estimates = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    # n : 문제의 수
    n = len(answers)
    for sequence in estimates:
        d, m = divmod(n, len(sequence))
        # score : 각 수포자들의 점수
        score = sum(int(answer == guess) for answer, guess in zip(answers, sequence*(d+1)))
        scores.append(score)
    
    for i, score in enumerate(scores):
        if score == max(scores):
            answer.append(i+1)
            
    return answer

# estimates : 각 수포자들의 찍기 조합
# n : 문제의 수
# score : 각 수포자들의 점수
# scores : 각 수포자들의 점수가 담긴 배열

# 1. 각 수포자들의 답안을 구한다.
# 2. 각 수포자들의 답안을 answer와 비교하여 점수를 구한다.
# 3. 가장 높은 점수를 얻은 수포자의 번호를 return 한다.