hangman = [
    """
  ______
  |    |      
  |          
  |        
  |    
  |   
 _|_
|   |______
|          |
|__________|
 
    """,
    """
  ______
  |    |      
  |    o      
  |       
  |    
  |   
 _|_
|   |______
|          |
|__________|
 
    """,
    """
  ______
  |    |      
  |    o      
  |    |    
  |    
  |   
 _|_
|   |______
|          |
|__________|
 
    """,
    """
  ______
  |    |      
  |    o      
  |   /|\     
  |    
  |   
 _|_
|   |______
|          |
|__________|
 
    """,
    """
  ______
  |    |      
  |    o      
  |   /|\     
  |    |
  |   
 _|_
|   |______
|          |
|__________|
 
    """,
    """
  ______
  |    |      
  |    o      
  |   /|\     
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|
 
    """,
]

def func():
    global run
    
    if count == 5 :
        print("Kind Man dies.")
        run = False
    hang = hangman[count]
    print(hang)
    print("Word_formed = "+ wordform)
    if wordform == word :
        run = False
        print("You Saved the life of a kid man.")



word = "Daksh"
wordform = "_"*len(word)
count = 0
# print(hangman[count])
func()
guessed_word = []
run = True
while run:
    guess = input("Guess_word : ")
    if guess in word.lower() :
        guessed_word.append(guess)
    else :
        count += 1
    stri = ""
    for i in word:
        if i.lower() in guessed_word:
            stri += i
        else:
            stri += "_"
    wordform = stri
    func()

