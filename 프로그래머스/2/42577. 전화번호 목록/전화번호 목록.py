def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        num = phone_book[i]
        if phone_book[i + 1].startswith(num):
            answer = False
            break
            
    return answer