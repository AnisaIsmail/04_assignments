ADULT_AGE = 18

def is_adult(age):
    return age >= ADULT_AGE

def main():
    age_input = input("How old is this person?: ")
    age = int(age_input)  
    print(is_adult(age))

if __name__ == '__main__':
    main() 