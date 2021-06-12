# -*- coding: utf-8 -*-


import csv

# Gathering quartiles for normalized scores
csv_file_stats = open("RatingData - Sheet1.csv", "r")
csv_reader_stats = csv.reader(csv_file_stats)

scores_ns = []
scores_nns = []
next(csv_reader_stats, None)
for row in csv_reader_stats:
    scores_ns.append(float(row[4]))
    scores_nns.append(float(row[8]))
csv_file_stats.close()
scores_ns.sort()
scores_nns.sort()

partitions_ns = []
print("Quintiles for native speaker ratings:")
for i in range(6):
    p = scores_ns[int(i * (len(scores_ns) - 1)/5)]
    partitions_ns.append(p)
    print(p)

partitions_nns = []
print("Quintiles for non-native speaker ratings:")
for i in range(6):
    p = scores_nns[int(i * (len(scores_nns) - 1)/5)]
    partitions_nns.append(p)
    print(p)
    
import matplotlib.pyplot as plt

print("Scores by native speakers")
plt.hist(scores_ns, 20)
plt.show()
print("Scores by non-native speakers")
plt.hist(scores_nns, 20)
plt.show()

# Helper function for labeling, specs defined by labeling schemes
def getLabel(index, value, is_ns):
    if index == 0:
        # Binary labeling
        return 0 if value < 0 else 1
    elif index == 1:
        # Strong Neutral
        return 0 if abs(value) <= 0.25 else (-1 if value < 0 else 1)
    elif index == 2:
        # Weak Neutral
        return 0 if abs(value) <= 0.75 else (-1 if value < 0 else 1)
    elif index == 3:
        # Labeling with Intermediates
        if value <= -1.5:
            return -2
        elif value >= 1.5:
            return 2
        return 0 if abs(value) <= 0.5 else (-1 if value < 0 else 1)  
    else:
        # Labeling with Partitions
        partitions = partitions_ns if is_ns else partitions_nns
        if value <= partitions[1]:
            return -2
        elif value >= partitions[4]:
            return 2
        elif value <= partitions[2]:
            return -1
        elif value >= partitions[3]:
            return 1
        return 0
    
csv_file = open("RatingData - Sheet1.csv", "r")
csv_reader = csv.reader(csv_file)

labels = ['ID', 'Message', 'NS', 'NNS']
filenames = ["BinaryLabeling.csv", "StrongNeutralLabeling.csv",
             "WeakNeutralLabeling.csv", "IntermediateLabeling.csv",
             "PartitionsLabeling.csv"]
fileobjs = [open("LabeledData/" + i, "w", newline='') for i in filenames]
writers = [csv.writer(i) for i in fileobjs]

# Gather statistics for each labeling scheme
counts_ns = [{} for i in filenames]
counts_nns = [{} for i in filenames]


for i in writers:
    i.writerow(labels)

bad_rows = 0
next(csv_reader, None)
for row in csv_reader:
    # Check for errors in comma division in csv
    if len(row) != 10:
        bad_rows += 1
    else:
        # Grabbing normalized scores from csv
        NS_score = float(row[4])
        NNS_score = float(row[8])
        
        # Performing labeling
        for i in range(len(filenames)):
            ns = getLabel(i, NS_score, True)
            nns = getLabel(i, NNS_score, False)
            writers[i].writerow([row[0], row[1], ns, nns])
            if ns in counts_ns[i]:
                counts_ns[i][ns] += 1
            else:
                counts_ns[i][ns] = 1
            if nns in counts_nns[i]:
                counts_nns[i][nns] += 1
            else:
                counts_nns[i][nns] = 1
csv_file.close()
for i in fileobjs:
    i.close()
print("Error rows:")
print(bad_rows)
print("\n\n")
for i in range(len(counts_ns)):
    print(filenames[i])
    print("Native speaker score frequencies:")
    print(counts_ns[i])
    print("Non-native speaker score frequencies:")
    print(counts_nns[i])
    print("\n")