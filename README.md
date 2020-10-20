# RelegramBotPython
WIth this simple code you will can send messages to Telegram


Make a bot with Telegram and Python.

In this document you can create a bot in Telegram for send messages into  channel,

The first step is download Telegram (if you don’t have), now you need create a new 
channel, the name of the channel is your desición, but for this example I will name it Test’ .


Now you need create a bot go to search bar an type in BotFather, choose it and send “/newbot” . You need a name for the Chat after you need the name of the bot. the messages looks like this:





Now go to channel and add members, in the search bar you type the name of the bot, select invite and made admin
 


Go the next step, copy the next URL and change the “<TOKEN>” for token’s bot    https://api.telegram.org/bot<TOKEN>/getUpdates  and you can’t visualize any information. Go again into Telegram and send a message inside of the channel 


Go back to the browser and refresh the url that you previously copied, now you can visualizate information. From this information you need the id chat for send messsages to that id that corresponds to the channel



Finally go to the code in python and replace your ID and TOKEN by yours and play send messages to the channel.



