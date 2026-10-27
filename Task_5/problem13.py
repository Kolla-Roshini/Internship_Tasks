# Problem: Nested Lists
# Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    
    unique_scores = sorted(list(set(score for name, score in records)))
    
   
    second_lowest_score = unique_scores[1]
    
    
    second_lowest_students = sorted([name for name, score in records if score == second_lowest_score])
    
    
    for student in second_lowest_students:
        print(student)