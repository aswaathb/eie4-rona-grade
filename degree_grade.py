# YEAR WEIGHTINGS
YRW_ONE = 0.111
YRW_TWO = 0.222
YRW_THREE = 0.333
YRW_FOUR = 0.334

# 4th Year split
YR_FOUR_FYP = 0.4
YR_FOUR_MOD = 0.6
YR_FOUR_NMOD = 7

year_grades = []

# Ask user for first 3 yr grades
for i in range(1,4):
    print("What was your grade (%) for year {}".format(i))
    grade = float(input())
    year_grades.append(grade)

# Fourth year modules assumed to count as whole module - i.e. (60/7)
 
# Ask user for 4th year modules - pre rona
print("IMPORTANT: This calculator assumes that for all pre-rona modules, 100% of the module is considered pre-rona.")
print("How many 4th yr modules count as pre-rona?")
num_pre_rona = int(input())

#reduced_yrw_four = num_pre_rona * (YR_FOUR_MOD/YR_FOUR_NMOD) * YRW_FOUR

pre_rona_grades = []
for i in range(1,num_pre_rona+1):
    print("Enter grade (%) for pre-rona module {}".format(i))
    mod_grade = float(input())
    pre_rona_grades.append(mod_grade)

avg_pre_rona_grades = sum(pre_rona_grades)/len(pre_rona_grades)

# calc guaranteed degree grade
guaranteed_deg_grade = 0
guaranteed_deg_grade += YRW_ONE   * year_grades[0]
guaranteed_deg_grade += YRW_TWO   * year_grades[1]
guaranteed_deg_grade += YRW_THREE * year_grades[2]
guaranteed_deg_grade += YRW_FOUR  * avg_pre_rona_grades
# update from KF - 4th yr weighting to stay the same
guaranteed_deg_grade /= (YRW_ONE+YRW_TWO+YRW_THREE+YRW_FOUR)

print("Your guaranteed degree grade is: {}".format(guaranteed_deg_grade))