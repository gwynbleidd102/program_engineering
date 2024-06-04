def is_palindrome(data: str) -> bool:
    return data == data[::-1]

if __name__ == "__main__":
    data = input().strip()
    if is_palindrome(data):
        print("YES")
    else:
        print("NO")