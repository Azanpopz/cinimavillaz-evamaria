class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href='https://t.me/EvaMariaBot'>𝙴𝚅𝙰 𝙼𝙰𝚁𝙸𝙰</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: 𝙹𝚘𝚑𝚗 𝙲𝚎𝚗𝚊
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/Joel_tg>𝖩𝗈𝖾𝗅 𝖳𝖦</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>𝖨 𝖺𝗆 𝖭𝗈𝗍 𝖠𝗇 𝖮𝗉𝖾𝗇 𝖲𝗈𝗎𝗋𝖼𝖾 𝖡𝗈𝗍 !</b>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. <a href=https://t.me/Cv_links_project7_bot>𝖩𝗈𝗁𝗇 𝖢𝖾𝗇𝖺</a> 𝗌𝗁𝗈𝗎𝗅𝖽 𝗁𝖺𝗏𝖾 𝖺𝖽𝗆𝗂𝗇 𝗉𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾.
2. 𝖮𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍.
3. 𝖠𝗅𝖾𝗋𝗍 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗁𝖺𝗏𝖾 𝖺 𝗅𝗂𝗆𝗂𝗍 𝗈𝖿 64 𝖼𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋𝗌.

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:</b>
• /filter - <code> 𝖺𝖽𝖽 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋 𝗂𝗇 𝖼𝗁𝖺𝗍
• /filters - <code> 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗈𝖿 𝖺 𝖼𝗁𝖺𝗍
• /del - <code> 𝖽𝖾𝗅𝖾𝗍𝖾 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖿𝗂𝗅𝗍𝖾𝗋 𝗂𝗇 𝖼𝗁𝖺𝗍
• /delall - <code> 𝖽𝖾𝗅𝖾𝗍𝖾 𝗍𝗁𝖾 𝗐𝗁𝗈𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍 (𝖼𝗁𝖺𝗍 𝗈𝗐𝗇𝖾𝗋 𝗈𝗇𝗅𝗒)"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- 𝖩𝗈𝗁𝗇 𝖢𝖾𝗇𝖺 𝖲𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗈𝗍𝗁 𝗎𝗋𝗅 𝖺𝗇𝖽 𝖺𝗅𝖾𝗋𝗍 𝗂𝗇𝗅𝗂𝗇𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌.

<b>𝖭𝖮𝖳𝖤:</b>
1. 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗐𝗂𝗅𝗅 𝗇𝗈𝗍 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝖺𝗇𝗒 𝖼𝗈𝗇𝗍𝖾𝗇𝗍, 𝗌𝗈 𝖼𝗈𝗇𝗍𝖾𝗇𝗍 𝗂𝗌 𝗆𝖺𝗇𝖽𝖺𝗍𝗈𝗋𝗒.
2. 𝖩𝗈𝗁𝗇 𝖢𝖾𝗇𝖺 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁 𝖺𝗇𝗒 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖾𝖽𝗂𝖺 𝗍𝗒𝗉𝖾.
3. 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝗌𝗁𝗈𝗎𝗅𝖽 𝖻𝖾 𝗉𝗋𝗈𝗉𝖾𝗋𝗅𝗒 𝗉𝖺𝗋𝗌𝖾𝖽 𝖺𝗌 𝗆𝖺𝗋𝗄𝖽𝗈𝗐𝗇 𝖿𝗈𝗋𝗆𝖺𝗍

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/cv_updatez)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. 𝖬𝖺𝗄𝖾 𝗆𝖾 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇 𝗈𝖿 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗂𝖿 𝗂𝗍'𝗌 𝗉𝗋𝗂𝗏𝖺𝗍𝖾.
2. 𝗆𝖺𝗄𝖾 𝗌𝗎𝗋𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝖽𝗈𝖾𝗌 𝗇𝗈𝗍 𝖼𝗈𝗇𝗍𝖺𝗂𝗇𝗌 𝖼𝖺𝗆 𝗋𝗂𝗉, 𝗉𝗈𝗋𝗇 𝖺𝗇𝖽 𝖿𝖺𝗄𝖾 𝖿𝗂𝗅𝖾𝗌.
3. 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝗍𝗁𝖾 𝗅𝖺𝗌𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗆𝖾 𝗐𝗂𝗍𝗁 𝗊𝗎𝗈𝗍𝖾𝗌.
 𝖨'𝗅𝗅 𝖺𝖽𝖽 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗍𝗁𝖺𝗍 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗆𝗒 𝖽𝖻."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- 𝖴𝗌𝖾𝖽 𝗍𝗈 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖻𝗈𝗍 𝗍𝗈 𝖯𝖬 𝖿𝗈𝗋 𝗆𝖺𝗇𝖺𝗀𝗂𝗇𝗀 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 
- 𝗂𝗍 𝗁𝖾𝗅𝗉𝗌 𝗍𝗈 𝖺𝗏𝗈𝗂𝖽 𝗌𝗉𝖺𝗆𝗆𝗂𝗇𝗀 𝗂𝗇 𝗀𝗋𝗈𝗎𝗉𝗌.

<b>NOTE:</b>
1. 𝖮𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇.
2. 𝖲𝖾𝗇𝖽 <code>/𝖼𝗈𝗇𝗇𝖾𝖼𝗍</code> 𝖿𝗈𝗋 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗇𝗀 𝗆𝖾 𝗍𝗈 𝗎𝗋 𝖯𝖬

<b>Commands and Usage:</b>
• <code>/𝖼𝗈𝗇𝗇𝖾𝖼𝗍  - 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝖼𝗁𝖺𝗍 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖯𝖬</code>
• <code>/𝖽𝗂𝗌𝖼𝗈𝗇𝗇𝖾𝖼𝗍  - 𝖽𝗂𝗌𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖿𝗋𝗈𝗆 𝖺 𝖼𝗁𝖺𝗍</code>
• <code>/𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌 - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗒𝗈𝗎𝗋 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /index  - <code>to add files from a channel</code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all tssa users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
