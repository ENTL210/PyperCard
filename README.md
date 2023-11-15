# Pypercard-Starter-Code
This is a little sample with some starter code to test out `pyscript` and the [`pypercard` module](https://pypercard.readthedocs.io/en/latest/index.html).

## Instructions
1. Clone or download this package.
2. Open the project in VSCode by double-clicking `pypercard_sample.code-workspace` (or opening the project folder with your favorite editor)
3. You'll need to run this on a local server - I recommend installing the Live Server extension for VSCode, but you may have another way to do this.
4. Read the [PyperCard Tutorials](https://pypercard.readthedocs.io/en/latest/tutorials.html) for specific details on what you can do.
5. Map out an idea for a "Choose Your Own Adventure" type game, quiz or questionnaire, or similar app.
    - If you don't know what to do, try one of the tutorials from step 4.
6. Explore lines 23-56 in pypercard.html to see the 3 card templates.
7. To add a card, be sure to copy the entire template code from one of the 3 templates and...
    - change the id value to card4
    - add the new card to the list of cards in `main.py` (starting at line 21)
8. Check out some of the options you have below.
9. Be sure to test out your code often.

## Things to try
### If you don't want a card to automatically advance to the next card
Remove the auto_advance and transition values from the card:
* from `Card("card3", auto_advance=5, transition="card1")`
* to `Card("card3")`

### Adding/editing buttons
To add a button, be sure to give it an ID

**In `pypercard.html` line 43 the ID is *reset***
`<button id="reset" autofocus>Reset</button>`
* Each id value in a web page must be unique

**In `main.py` lines 34 - 36**
```
@carousel_app.transition("card2", "click", "reset")
def reset(app, card):
    return "card1"
```
* `"card2"` represents the card where the button is found
* `"click"` is the interaction made with the button.
* `"reset"` is the name of the id

To have a button in card3 go to card2 when clicked, you could add the following:
**In `pypercard.html` somewhere inside the `<template id="card3>` tag just after the last `<p>` tag, add...**
`<button id="goto_card2" autofocus>Go back a card</button>`

**Then, in main.py, add the following...**
```
@carousel_app.transition("card3", "click", "go_back")
def go_back(app, card):
    return "card2"```

### This should get you started.
One last thing: have fun!