import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("students.csv")
clean_df = df.dropna().copy()

# This function calculates a statistical reports and prints out all statistic calculations. 
def statistics():
    print()
    print("Statistical Report: ")
    mean = clean_df["Grade"].mean()
    median = clean_df["Grade"].median()
    std = clean_df["Grade"].std()
    max_grade = clean_df["Grade"].max()
    min_grade = clean_df["Grade"].min()
    clean_df["Above_Avg"] = clean_df["Grade"] > mean
    above_avg_count = clean_df["Above_Avg"].value_counts()
    clean_df["Below_Avg"] = clean_df["Grade"] < mean
    below_avg_count = clean_df["Below_Avg"].value_counts()
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std:.2f}")
    print("Max:", max_grade)
    print("Min:", min_grade)
    print("Students above average:", above_avg_count.get(True, 0))
    print("Students below average:", below_avg_count.get(True, 0))    
    return mean

# This function prints the top 3 and bottom 3 performing students. 
def top_and_bottom():
    sorted_df = clean_df.sort_values("Grade", ascending=False)

    top3 = sorted_df.head(3)
    bottom3 = sorted_df.tail(3)

    print("The top 3 students are: ")
    for i, row in top3.iterrows():
        print(row["Name"], ":", row["Grade"])

    print()

    print("The bottom 3 students are: ")
    for i, row in bottom3.iterrows():
        print(row["Name"], ":", row["Grade"])

# This function displays the data in a bar graph, and includes a red line, which shows the average grade. 
def bar_chart(mean):
    plt.bar(clean_df["Name"], clean_df["Grade"])
    plt.title("Students Grade")
    plt.xlabel("Students")
    plt.ylabel("Grade")
    plt.xticks(rotation=45)
    plt.axhline(mean, color="red", linestyle="--", label="Class Average")
    plt.legend()

    plt.tight_layout()
    plt.savefig("bar_chart.png", dpi = 300)
    plt.show()

# This function displays the distribution of the grades through a histogram. 
def hist():
    plt.hist(clean_df["Grade"], bins=5)
    plt.title("Grade Distribution")
    plt.xlabel("Grade Range")
    plt.ylabel("Number of students")

    plt.tight_layout()
    plt.savefig("histogram.png", dpi = 300)
    plt.show()


mean_val = statistics()
print()
top_and_bottom()
print()
bar_chart(mean_val)
print()
hist()






