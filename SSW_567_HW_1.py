def classify_triangle(a,b,c):    #creating function
    if a == b == c:
        return 'equilateral'
    elif a == b or a == c or b == c:
        return 'iscocoles'
    elif a*a + b*b == c*c or c*c + b*b == b*b or a*a + c*c == a*a:
        return 'right'
    else:
        return 'scalene'

print('The triangle is a ' + classify_triangle(2,2,4) + ' triangle')