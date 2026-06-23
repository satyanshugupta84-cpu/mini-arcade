import streamlit as st
import random

st.set_page_config(page_title="Game Zone", page_icon="🎮")

st.title("🎮 Mini Aacred")

game = st.sidebar.selectbox(
    "Choose a Game",
    ["Snake Water Gun", "Rock Paper Scissors", "Number Guessing"]
)

# ---------------- Snake Water Gun ----------------
if game == "Snake Water Gun":
    st.header("🐍 Snake Water Gun")

    choices = {"Snake": 1, "Water": -1, "Gun": 0}
    user_choice = st.selectbox("Choose", list(choices.keys()))

    if st.button("Play Snake Game"):
        computer = random.choice([-1, 0, 1])
        you = choices[user_choice]

        reverseDict = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}

        st.write("You chose:", reverseDict[you])
        st.write("Computer chose:", reverseDict[computer])

        if computer == you:
            st.warning("🤝 Draw!")
        elif (computer == -1 and you == 1) or \
             (computer == 1 and you == 0) or \
             (computer == 0 and you == -1):
            st.success("🎉 You Win!")
            st.balloons()
        else:
            st.error("😢 You Lose!")

# ---------------- Rock Paper Scissors ----------------
elif game == "Rock Paper Scissors":
    st.header("✊ Rock Paper Scissors")

    options = ["Rock", "Paper", "Scissors"]
    user = st.selectbox("Choose", options)

    if st.button("Play RPS"):
        computer = random.choice(options)

        st.write("You:", user)
        st.write("Computer:", computer)

        if user == computer:
            st.warning("Draw!")
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Paper" and computer == "Rock") or \
             (user == "Scissors" and computer == "Paper"):
            st.success("You Win!")
        else:
            st.error("You Lose!")

# ---------------- Number Guessing ----------------
elif game == "Number Guessing":
    st.header("🔢 Number Guessing")

    number = random.randint(1, 10)
    guess = st.number_input("Guess number (1-10)", 1, 10)

    if st.button("Check Number"):
        if guess == number:
            st.success("🎉 Correct!")
            st.balloons()
        else:
            st.error(f"Wrong! Number was {number}")