def f(word,path):
    if len(word) == 0:
        return True
    else:
        print word,path
        a = path[-1][0]
        b = path[-1][1]
        if a != 0 and [a-1,b] not in path:
            if board[a-1][b] == word[0]:
                
                if f(word[1:],path+[[a-1,b]]):
                    return True
     
        if a != len(board)-1 and [a+1,b] not in path:
            if board[a+1][b] == word[0]:
                
                if f(word[1:],path+[[a+1,b]]):
                    return True
      
        if b != 0 and [a,b-1] not in path:
            if board[a][b-1] == word[0]:
               
                if f(word[1:],path+[[a,b-1]]):
                    return True
        if b != len(board[0])-1 and [a,b+1] not in path:
            if board[a][b+1] == word[0]:
                
                if f(word[1:],path+[[a,b+1]]):
                    return True
        return False
        
board = [
  ["A",'A'],
  
        ]	
word = 'AAA'	
for i in xrange(len(board)):
	for j in xrange(len(board[0])):
		if board[i][j] == word[0] and f(word[1:],[[i,j]]):
			print True
print False