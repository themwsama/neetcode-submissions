class Solution:
    def calPoints(self, operations: List[str]) -> int:
        recorded_scores = []

        for i in range(len(operations)):
            if operations[i] == "+":
                second = recorded_scores[-1]
                first = recorded_scores[-2]
                total = first + second
                recorded_scores.append(total)

            elif operations[i] == "C":  
                recorded_scores.pop()
            elif operations[i] == "D":
                score = recorded_scores[-1]
                recorded_scores.append(int(score) * 2)
            else:
                print(operations[i])
                recorded_scores.append(int(operations[i]))



        return sum(recorded_scores)