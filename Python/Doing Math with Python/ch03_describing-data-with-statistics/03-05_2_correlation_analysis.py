'''
Purpose: Find the coorelation for college admission test score with other factor
Author: Yasen Zhao
Date: 2024/02/17
'''

def find_corr_x_y(x,y):
    n = len(x)
    
    # Find the sum of the products
    prod = []
    for xi, yi in zip(x,y):
        prod.append(xi*yi)
    
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2
    
    x_square = []
    for xi in x:
        x_square.append(xi ** 2)
    x_square_sum = sum(x_square)
    
    y_square = []
    for yi in y:
        y_square.append(yi ** 2)
    y_square_sum = sum(y_square)
    
    # use formula to calculate correlation
    numerator = n * sum_prod_x_y - sum_x * sum_y
    denominator_term1 = n * x_square_sum - squared_sum_x
    denominator_term2 = n * y_square_sum - squared_sum_y
    denominator = (denominator_term1 * denominator_term2) ** 0.5
    
    correlation = numerator / denominator
    
    return correlation

if __name__ == '__main__':
    
    # high_school_grades = [90,92,95,96,87,87,90,95,98,96]
    # colleage_admission_score = [85,87,86,97,96,88,89,98,98,87]
    # if (len(high_school_grades)==len(colleage_admission_score)):
    #     print('The correlation of \n{0} \nand \n{1} \nis: {2:.2f}'.format(high_school_grades, colleage_admission_score, find_corr_x_y(high_school_grades,colleage_admission_score)))
    # else:
    #     print('dismatch on the data sets length')
    
    high_school_math_grades = [83,85,84,96,94,86,87,97,97,85]
    colleage_admission_score = [85,87,86,97,96,88,89,98,98,87]
    if (len(high_school_math_grades)==len(colleage_admission_score)):
        print('The correlation of \n{0} \nand \n{1} \nis: {2:.5f}'.format(high_school_math_grades, colleage_admission_score, find_corr_x_y(high_school_math_grades,colleage_admission_score)))
    else:
        print('dismatch on the data sets length')