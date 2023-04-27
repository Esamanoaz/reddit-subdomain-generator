filename = 'domain-list.txt'
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
         'h', 'i', 'j', 'k', 'l', 'm', 'n', 
         'o', 'p', 'q', 'r', 's', 't', 'u', 
         'v', 'w', 'x', 'y', 'z']
url = '.reddit.com'
redirect = '127.0.0.1'

with open(filename, 'w') as f:
    for i in range(len(alpha)):
        first = alpha[i]
        for j in range(len(alpha)):
            second = alpha[j]
            f.write(redirect + ' ' + first + second + url + '\n')