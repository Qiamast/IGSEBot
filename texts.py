START_MSG = (
    "Hey [{first_name}](tg://user?id={chat_id})!\n\n"
    "I'm *IGSE* 🤖, inline Google search tool for telegram 🌐.\n\n"
    "Send /help to get started and see the instructions 📖."
)
HELP_MSG = (
    "📖 *IGSE Bot Usage*\n\n"
    "To search for any title, just type my username and the query you want to search 🔎\n"
    "\n*Examples* 🧪 \n\n"
    "🔸 `@IGSEBot how to be hiro` - search results about of query\n"
    "🔸 `@IGSEBot flower page:2` - search results about of query on page 2\n"
    "\n❗ Beside the query, you can add commands to change the search results behavior.\n\n"
    "*Supported commands*:\n\n"
    "🔸 `page:<number>`: Change the page of the search results (default: 1)\n"
    "\n💡 *Note:*\n\n"
    "The search results are paginated. You can change the page "
    "of the search results by adding a command to the query.\n"

)
NOT_FOUND_MSG = (
    "Sorry, I couldn't find any results for your query 😔"
)
SPELLING_MSG = (
    "💡 Did you mean {corrected_query!r} instead?"
)
PRIVATE_SEARCH_MSG = (
    "Press the button below to search for *{query!r}* "
    "in this chat 👇🏻"
)

OUTPOT_MSG = (
    "[{title}]({url})🔍"
)
