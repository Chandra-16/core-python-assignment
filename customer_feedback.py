def feedback(ratings):

    if not ratings:
        return 0
    positive = sum(1 for r in ratings if r >= 4)
    return (positive / len(ratings)) * 100


ratings = list(map(int, input("Enter ratings (1-5) space separated: ").split()))

prcntg = feedback(ratings)
print(f"Positive Feedback: {round(prcntg, 2)}%")