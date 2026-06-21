import json
import random
import time

path = r"C:\Users\Pratham\OneDrive\Desktop\python\question.json"
with open(path) as f:
    data = json.load(f)

s = 0
difficulty = input("Choose difficulty level(easy😇/medium😃/hard😥/super_hard😈) :")
print("You have 60 seconds for Every Question ⏳")
question = data[difficulty]
random.shuffle(question)
question = random.sample(question, 5)

for i, q in enumerate(question, start=1):
    start = time.time()
    print(f"\n{i}." + q["question"])
    for key, val in q["options"].items():
        print(f"{key}){val}")
    user_a = input("Enter the correct option(A/B/C/D) :").upper()

    end = time.time()
    if end - start < 60:
        print("✅ Anwser Accepted")
    else:
        print("⏰ Time Over")

    if user_a == q["answer"]:
        print("✅ Correct")
        s += 1
    else:
        print("❌ Wrong ")
        print("Correct option = ", q["answer"])

print(f"Result : {s} / {len(question)}")
