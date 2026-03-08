# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

--- Initially the issue that I saw is that it had a list for display for history and that the ranging for scoring were inaccurate as Normal was 3rd tier for return value when Hard should be and vice versa. It also was telling me to go higher when I was already at 100 so it was out of range. 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- THe AI LLM I used was Claude where I ran a diagnosis of each function to ensure that it was computing its intended purpose via return response. One example is that I immediately saw that the get_range_for_difficulty was inaccurate in returning the proper output and could use some refactoring as well. UI hardcodes "1 and 100" regardless of difficulty as well.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I wanted to run tests to ensure that the function was being executed properly. One of the tests that I ran was for the show hint which didn't show a hint properly and utilized AI to invert the messages properly. AI helped me design the tests to match specific guidelines and guiding points that it suggested after confirmation to allow those changes. 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- This was my first time working with Streamlit, and the biggest thing I had to wrap my head around was how it handles state. Unlike a traditional app things usually stay in memory, Streamlit reruns your entire Python script from top to bottom every single time the user interacts with anything — clicking a button, toggling a checkbox, typing in a field. That means any regular variable you set during one run is completely gone by the next. To keep things like the score, attempt count, or guess history alive between interactions, you have to store them in `st.session_state`, which is basically a dictionary that Streamlit preserves across reruns. If you don't use it, your app has amnesia. That's exactly why bugs like the hint disappearing happened — the hint was a local variable that died at the end of each rerun instead of being saved in session state.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--- One habit I want to carry forward is diagnosing each function individually before trying to fix everything at once. Breaking the bugs down into phases and verifying each fix with tests before moving on kept things from snowballing. Next time I work with AI on a coding task, I'd be more careful about verifying its output line by line rather than trusting that it works just because it looks right The project proved that AI-generated code can look clean and still be full of subtle bugs. It changed how I think about AI code in general: it's a solid starting point for sure, but you still required to be the one who actually understands what the code is doing and catches what it gets wrong.
