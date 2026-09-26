measurements = [18, 21, 24, 19]
review_threshold_text = "20"

# Testing
# measurements = [21, 30, 11, 9]
# review_threshold_text = "15"

# Replace this scaffold output with your calculation, loop, decision, and summary.
# print("TODO: complete the measurement summary")
review_threshold = int(review_threshold_text)
total = 0
review_count = 0
count = 0
for measurement in measurements:
    total += measurement
    count += 1
    if measurement >= review_threshold:
        print("Measurement:", measurement, "review")
        review_count += 1
    else:
        print("Measurement:", measurement, "within range")

mean = total / count
print("Count:", count)
print("Total:", total)
print("Mean:", mean)
print("Review Count:", review_count)