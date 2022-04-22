# GROUP MEMBERS        Roll no.        PRN
# Sanskruti Jaiswal    222028          22010690
# Kirti singh          222037          22010254
# Manya Gupta          222041          22010316
 
import pandas as pd # To use CSV files, we used pandas
df=pd.read_csv(r'C:/Users/hp/Downloads/ps.csv') # Reading CSV file which ciontains the height data of the students
from scipy.stats import ttest_1samp  # for t-test hypothesis
import numpy as np #for numerical calculations

def hypo_test():

    print("****************************************************************************************************************")
    print("\n                               HYPOTHESIS  TESTING  USING  T - TEST                                            ")
    print("\n****************************************************************************************************************")
    print("\n ___________________________ Sample Data of Student's Height ______________________________\n")
    print(df) # printing the data of CSV file
    HEIGHT_MEAN = np.mean(df) #Calculating mean  value taking the data of CSv file
    print("Number of Sample data = 10")
    print("*****Mean height of students*****")
    print(HEIGHT_MEAN) # Printing mean value
    n = int(input("Enter the null Hypothesis value: ")) # taking the null hypothesis value from the user
    tset, pval = ttest_1samp(df, n) # calculating p-value
    los = float(input("Enter the level of significance: ")) # taking the  value of level of significance from the user
    print("p-values",pval) 
    # checking the conditions to accept or reject the null hypothesis
    if pval < los: 
        print("Since value of alpha = ", los)   
        print(" we are rejecting null hypothesis")
    else:
        print("Since value of alpha = ",los)
        print("we are accepting null hypothesis")

    print("Do you want to continue... If yes press Y otherwise N")
    select = input("Enter Your Choice: ")
    if (select == 'Y' or select == 'y') :
        hypo_test() 
    else:
        print("BYE BYE......")       

hypo_test()
