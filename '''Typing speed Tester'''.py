'''Typing speed Tester'''
import time
s="The quick brown fox jumps over the lazy dog."
print("Type the following sentence exactly as shown:\n")
print(s)
input("Press Enter when you're ready to start...\n")
start_time=time.time()
typed=input("Start typing: ")
end_time=time.time()
time_taken=round(end_time - start_time, 2)
# Accuracy calculation
correct_chars=0
for i in range(min(len(s), len(typed))):
    if s[i]==typed[i]:
        correct_chars+=1

accuracy = (correct_chars / len(s)) * 100

# Calculate words per minute (WPM)
words=len(s.split())
wpm=(words / time_taken) * 60

# Show results
print("\nResults")
print(f"Time Taken: {time_taken} seconds")
print(f"Typing Speed: {round(wpm)} WPM")
print(f"Accuracy: {round(accuracy)}%")