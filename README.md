# TOC Project 2017

### Prerequisite
* Python 3

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "play a"
		* Reply: the corresponding question "Basic Problem--SET"
		* When user's answer is correct, it would reply 'correct'
		* When user's answer is wrong, it would reply 'wrong'
		* User can type 'answer' to get the official answer with a picture to explain it.
		* User can type 'back' to get back to the initial state.

	* Input: "play b"
		* Reply: the corresponding question "Technical Problem--EAT"
		* When user's answer is correct, it would reply 'correct'
		* When user's answer is wrong, it would reply 'wrong'
		* User can type 'answer' to get the official answer with a picture to explain it.
		* User can type 'back' to get back to the initial state.
	
	* Input: "play c"
		* Reply: the corresponding question "Technical Problem--BROKE EYE"
		* When user's answer is correct, it would reply 'correct'
		* When user's answer is wrong, it would reply 'wrong'
		* User can type 'answer' to get the official answer with a picture to explain it.
		* User can type 'back' to get back to the initial state.
		
	* Input: "play d"
		* Reply: the corresponding question "Advanced Problem--DEATH LIVE"
		* When user's answer is correct, it would reply 'correct'
		* When user's answer is wrong, it would reply 'wrong'
		* User can type 'answer' to get the official answer with a picture to explain it.
		* User can type 'back' to get back to the initial state.
