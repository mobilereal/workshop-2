score = int(input("Enter your score: "))

print
if (score >= 80) and (score <= 100):
    print("grade: A")
elif (score >= 75) and (score <= 79):
    print("grade: B+")
elif (score >= 70) and (score <= 74):
    print("grade: B")
elif (score >= 65) and (score <= 69):
    print("grade: C+")
elif (score >= 60) and (score <= 64):
    print("grade: C")
elif (score >= 55) and (score <= 59):
    print("grade: D+")
elif (score >= 50) and (score <= 54):
    print("grade: D")
elif (score >= 0) and (score <= 49):
    print("grade: F")
