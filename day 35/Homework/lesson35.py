#Homework 1:

print(type("Hello, World!"))    #ეს კოდი გამოიტანს stringს რადგან print(type) ამოწმებს მონაცემის ტიპს, ხოლო "Hello, World!" არის stirng(str)

#Homework 2:



#Homework 3:

for i in range(10):
    print(i)

#Homework 4:

print("Hello" + "World")

#Homework 5:

#real არ არის სწორი მონაცემთა ტიპი:
a = 1
print(str(a))   #str ყოფილა მონაცემის ტიპი

b = "5"
print(int(b))    #int ყოფილა მონაცემის ტიპი


c = 1, 2, 3
print(list(c))    #list ყოფილა მონაცემთა ტიპი

#Homework 6:

user_info = int(input("How old are you?"))

#Homework 7:

for i in range(5):
#↑ (keyword)
   print(i)

#Homework 8:

num = 3
print(float(num))

#Homework 9:

print(2 > 3)    #ეს კოდი დაბეჭდავს False-ს იმიტომ, რომ მართლაც 2 > 3 არის მცდარი(False) და ასევე იმიტომ, რომ არ არის str

#Homework 10:

while True:
    i = 10
    print(i)

#Homework 11:
print("Hello "+"World")    #ეს დაბეჭდავს Hello World

#Homework 12:

print(4%2)   #ეს დაბეჭდავს 0-ს რადგან 4 რომ გავყპთ 2 ზე ნაშთი იქნება  0

#Homework 13:

#როგორც ხედავთ ყველა ჩემი პითონის ფაილი ბოლოვდება .py თი

#Homework 14:

print(10==10)  #ეს დაბეჭდავს True-ს, რადგან 10 მართლაც 10-ს უდრის, ანუ არის სიმართლე(True)

#Homework 15:

#სწორი ცვლადის სახელია:
_var_name = 1
#ეს ცვლადის სახელი იმიტომ არის სწორი, რომ მასში არაა დაშორება(space), მისი პირველი სიმბოლო არ არის რიცხვი(1,2,3,4...)

#არასწორი ცვლადის სახელებია:
#2nd_var. ამ ცვლადის სახელი იმიტომ არის არასწორი, რომ მისი პირველი სიმბოლოა რიცხვი, 2
#var-name. ამ ცვლადის სახელი იმიტომ არის არასწორი, რომ მისი ერთერთი სიმბოლო _ ის ნაცვლას - არის
#var name. ამ ცვლადის სახელი იმიტომ არის არასწორი, რომ აქ არის გამოყენებული დაშორება(space), რომელიც არასწორია და შეგვიძლია ჩავანაცვლოთ _ თი 

#Homework 16:

print('5'*5)  #ეს კოდი დაბეჭდავს 555-ს, რადგან მისი პირველი ნამრავლი სტრინგია, ხოლო მეორე კი მთელი რიცხვი

#Homework 17:

print('Hello'[-1])    #ეს კოდი დაბეჭდავს o-ს, რადგან -1 ნიშნავს ელემენტის ბოლო სიმბოლოს, ანუ o-ს

#Homework 18:

print(list(range(2, 10, 2)))    #ეს კოდი დაბეჭდავს [2, 4, 6, 8]-ს, რადგან პირველ რიგში ვნახოთ range() ფუნქციაში რა ხდება. range(2, 10, 2) პირველი ციფრი, 2 ნიშNავს, რომ ათვლა დაიწყება 2 დან, ხოლო 10 ნიშნავს, რომ 10 მდე გაგრძელდეს ეს ათვლა, ხოლო ბოლოში რომ არის კიდევ ერთი 2 იანი ეს ნიშნავს, რომ ამ ათვლაში მხოლოდ დაწეროს ის რიცხვები, რომელიც იყოფა ორზე უნაშთოდ, list ნიშნავს, რომეს ყველა რიცხვი გადმოგვცეს სიის სახით

#Homework 19:

print(list(range(2, 10, 2)))    #ეს კოდი დაბეჭდავს [2, 4, 6, 8]-ს, რადგან პირველ რიგში ვნახოთ range() ფუნქციაში რა ხდება. range(2, 10, 2) პირველი ციფრი, 2 ნიშNავს, რომ ათვლა დაიწყება 2 დან, ხოლო 10 ნიშნავს, რომ 10 მდე გაგრძელდეს ეს ათვლა, ხოლო ბოლოში რომ არის კიდევ ერთი 2 იანი ეს ნიშნავს, რომ ამ ათვლაში მხოლოდ დაწეროს ის რიცხვები, რომელიც იყოფა ორზე უნაშთოდ, list ნიშნავს, რომეს ყველა რიცხვი გადმოგვცეს სიის სახით

#Homework 20:

#while ციკლი შეიძლება განმეორდეს უსასრულოდ, თუ პირობა სულ სწორი იქნება(while True), მაგ:
while True:
    print(10 == 10)

#Homework 21:
#True და False არის ბულიანები
#Homework 22:
#1 <= 1 არის True(ჭეშმარიტი)
#Homework 23:
#მაგალითი 1:
print(10 != 10 and 10 == 10)

#მაგალითი 2:
print(1 > 2 and 2 < 1)

#მაგალითი 3:
print(5 > 0 and 0 < 5)
#Homework 24:
my_list = [10 , 20, 30, 40]   #10 არის მენულე ელემენტი, 20 არის პირველი ელემენტი, 30 არის მეორე ელემენტი და 40 არის მესამე
print(my_list[2])
#Homework 25:
list = [1, 2, 3]  #ეს არის სწორი სია
#Homework 26:
#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>Document</title>
#</head>
#<body>
#<!--HTML - HyperText Markup Language-->

#</body>
#</html>

#Homework 27:
#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Document</title>
#    <!--აქ არის საიტის ტექნიკური ინფორმაცია, რომელიც ინახება <head> თაგში-->
#</head>
#<body>
    
#</body>
#</html>

#Homework 28:

#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>Document</title>
#</head>
#<body>
#    <a href="რამე ლინკი">ლინკი</a>
#</body>
#</html>

#Homework 29:

#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Document</title>
#</head>
#<body>
#    <h1>ყველაზე დიდი სათაური</h1>
#</body>
#</html>

#Homework 30:

#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Document</title>
#</head>
#<body>
#    <!--იყენება alt ი-->
#</body>
#</html>

#Homework 31:

#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>დოკუმეტის სათაური</title>
#</head>
#<body>
    
#</body>
#</html>

#Homework 32:

#<!DOCTYPE html>
#<html lang="en">
#<head>
#   <meta charset="UTF-8"> #   
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>Document</title>
#</head>
#<body>
#    <p>Hello <br> world</p>
#</body>
#</html>

#Homework 33:

#<!DOCTYPE html>
#html lang="en">
#<head>
#    <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Document</title>
#</head>
#<body>
#   <!--ul - unordered list(დაულაგებელი სია)-->
#</body>
#</html>

#Homework 34:

#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>Document</title>
#</head>
#<body>
#    <input type="checkbox" name="ia" id="ai">
#</body>
#</html>

#Homework 35:

#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Document</title>
#</head>
#<body>
#    <p style="color: green;">GoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaGoaaGoaGoaGoaGoaGoaGoaGoa</p>
#</body>
#</html>

#Homework 36:

#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Document</title>
#</head>
#<body>
#      <input type="Hello, World!" name="Hello" id="World">
#</body>
#</html>

#Homework 37:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <a href="კიდევ ერთი ლინკი"></a>
</body>
</html>

#Homework 38:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p><em>Hello, Goa!</em></p>
</body>
</html>

#Homework 39:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="action, GOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"></form>
</body>
</html>

#Homework 40:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p id="გამორჩეული">GOA</p>
</body>
</html>

#Homework 41:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!--ol - ordered list(დალაგებული სია)-->
</body>
</html>

#Homework 42:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <select name="Goa is" id="the best"></select>
</body>
</html>

#Homework 43:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <nav>
        <!--nav - ნავიგაციის ღილაკი-->
    </nav>
</body>
</html>

#Homework 44:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <main>
        <p>მთავარი ნაწილი</p>
    </main>
</body>
</html>

#Homework 45:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!--კომენტარი არის ეს-->
</body>
</html>

#Homework 46:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <input type="text" required> 
</body>
</html>

#Homework 47:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <img src="სურათი" alt="">
</body>
</html>

#Homework 48:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <audio src="რამე სიმღერა, აუდიო"></audio>
</body>
</html>

#Homework 49:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <video src="აქ რამე ვიდეო"></video>
</body>
</html>

#Homework 50:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>რათქმაუნდა GOA > დანარჩენი პროგრამირების აკადემიები</p>
    <!--GOA = mogger
        other programming academies = mogged bye the allmighty GOA-->
</body>
</html>

