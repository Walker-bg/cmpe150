def is_pangram(s):
    s=s.lower()
    chars = ['z','x','c','v','b','n','m','a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p']
    for char in chars:
        if char not in s:
            print("False")
            return False
    print("True")
    return True

is_pangram("A quick brown fox jumps over the lazy dog.")
is_pangram("A quart jar of oil mixed with zinc oxide makes a very bright paint.")
is_pangram("A quick movement of the enemy will jeopardize six gunboats.")
is_pangram("A quick movement of the enemy ill jeopardie si gunboats")