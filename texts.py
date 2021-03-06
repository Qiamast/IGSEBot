START_MSG = (
    "Hey [{first_name}](tg://user?id={chat_id})!\n\n"
    "I'm *{bot_username}* ๐ค, inline Google search tool for telegram ๐.\n\n"
    "Send /help to get started and see the instructions ๐."
)
HELP_MSG = (
    "๐ *{bot_username} Bot Usage*\n\n"
    "To search for any title, just type my username and the query you want to search ๐\n"
    "\n*Examples* ๐งช \n\n"
    "๐ธ `@{bot_username} how to be hiro` - search results about of query\n"
    "๐ธ `@{bot_username} flower :2` - search results about of query on page 2\n"
    "\nโ Beside the query, you can add commands to change the search results behavior.\n\n"
    "*Supported commands*:\n\n"
    "๐ธ `:<number>`: Change the page of the search results (default: 1)\n"
    "\n๐ก *Note:*\n\n"
    "The search results are paginated. You can change the page "
    "of the search results by adding a command to the query.\n"

)
NOT_FOUND_MSG = (
    "Sorry, I couldn't find any results for your query ๐"
)
SPELLING_MSG = (
    "๐ก Did you mean {corrected_query!r} instead?"
)
PRIVATE_SEARCH_MSG = (
    "Press the button below to search for *{query!r}* "
    "in this chat ๐๐ป"
)

OUTPOT_MSG = (
    "[{title}]({url})๐"
)
