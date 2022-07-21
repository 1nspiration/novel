init python: # создание объекта класса
 Player = player()  
   
   
label start:
    "О, мы уже начали. Приветсвую тебя, тебя..."
    $name = renpy.input("Как тебя звать?")
    scene bg roof of the house
    show player at top 
    "ну тут типо мысли прыгать или нет"
label questions:    
    menu:
        "ну тут типо мысли прыгать или нет"
        
        "Прыжок 1":
         $player.mental_condition-=1
         jump wake_up
         
        "Прыжок 2":
         $player.mental_condition-=3
         jump wake_up
        
        "Прыжок 3":
         $player.mental_condition-=5
         jump wake_up

label wake_up:

    scene bg camp house
    with fade
    show player at left
    "Тут, наверное, мысли типо: че за нахуй,где я и т.д"
    show D at right
    "Димон появляется и ты думаешь, что спросить"
    
label questions_to_D:
    menu:
        "Че спросить?"
        
        "Вариант 1":
         jump dialog_for_D1
         $player.sympathy_dima+=2
         $player.mental_condition+=3
       
        
        "Вариант 2":
         $player.mental_condition-=3
         jump dialog_for_D2
        
        "Вариант 3":
         $player.sympathy_dima-=2
         $player.mental_condition-=3
         jump dialog_for_D3
        
label dialog_for_D1:
    "Диалог"
    jump dialog_for_W
    
label dialog_for_D2:
    "Диалог"
    jump dialog_for_W
    
label dialog_for_D3:
    "Диалог"
    jump dialog_for_W
    
label dialog_for_W:
    scene bg camp house
    show player at left
    show W at right
    "Тут видимо диалог"
    jump outside
label outside:
    scene outside
    with fade
    #я чет не особо понял, что здесь происходит, написал как понял
    "Что это было?"
label questions2:
    menu:
        "Что это было?"
        
        "Промолчать":
         jump dialog_for_O
         
        "Что ты толко что пытался достать":
         $player.epiphany +=1
         jump dialog_for_O
         
label dialog_for_O:
    scene outside
    with fade
    show player at left
    show W at left
    show O at right
    "О чем она"

label questions_to_O:
    menu:
        "О чем она?"
      
        "О чем ты":
         $player.sympathy_vera -=2
         jump go_to_counselor
        
        
        "Ах да, конечно":
         $player.sympathy_vera -=2
         jump go_to_counselor
         
label go_to_counselor:
    "Идет к вожатой"
    return