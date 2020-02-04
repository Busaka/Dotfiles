import subprocess
config.load_autoconfig()
# exec(open("/home/ll/.bin/mm.py").read())

c.spellcheck.languages = ['en-GB']
c.auto_save.session = True
c.completion.cmd_history_max_items = 1000
c.completion.scrollbar.padding = 0
c.content.headers.accept_language = "en-GB,en,en-US"
c.content.notifications = "ask"
c.content.user_stylesheets = ["style.css"]
c.downloads.open_dispatcher = "xdg-open"
c.downloads.position = "bottom"
c.input.insert_mode.auto_load = False
c.messages.timeout = 3000
c.editor.command = ["st", "-e", "nvim", "{}"]
c.prompt.radius = 0
# c.scrolling.bar = "never"
c.scrolling.bar = "always"
c.scrolling.smooth = True
c.statusbar.padding = {"top": 0, "right": 0, "bottom": 0, "left": 0}
c.statusbar.widgets = ["url", "scroll_raw", "progress"]
c.tabs.background = True
#c.tabs.favicons.scale = 2
#c.tabs.indicator.padding = {"top": 0, "right": 0, "bottom": 0, "left": 0}
c.tabs.position = "top"
c.tabs.show = "always"
# c.tabs.show_switching_delay = 2000
# c.tabs.title.format = ""
# c.tabs.title.format_pinned = c.tabs.title.format
# c.tabs.width = 24
# c.tabs.indicator.width = 0
c.tabs.padding = {"top": 3, "right": 3, "bottom": 3, "left": 3}
c.url.start_pages = "about:blank"
c.url.default_page = "https://www.google.com"
c.downloads.location.prompt = False
c.content.geolocation = False
c.content.ssl_strict = True
#c.downloads.remove_finished = 800
c.hints.dictionary = "/usr/share/dict/british"
c.url.searchengines = {"DEFAULT": "https://google.com/search?&q={}",
"dd": "https://www.duckduck.com/?q={}",
"ggi": "https://www.google.co.uk/search?q={}&tbm=isch",
"w": "https://en.wikipedia.org/w/index.php?search={}",
"st": "http://store.steampowered.com/search/?term={}",
"g": "https://duckduckgo.com/?q={}",
"mw": "http://en.uesp.net/w/index.php?title=Special%3ASearch&search={}",
"aur": "https://aur.archlinux.org/packages/?O=0&K={}",
"pac": "https://www.archlinux.org/packages/?sort=&arch=x86_64&maintainer=&flagged=&q={}",
"aw": "https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}",
"gw": "https://wiki.gentoo.org/index.php?title=Special%3ASearch&search={}&go=Go",
"i": "http://www.imdb.com/find?ref_=nv_sr_fn&s=all&q={}",
"dick": "https://en.wiktionary.org/wiki/{}",
"ety": "http://www.etymonline.com/index.php?allowed_in_frame=0&search={}",
"u": "http://www.urbandictionary.com/define.php?term={}",
"y": "https://www.youtube.com/results?search_query={}",
"r": "https://www.reddit.com/r/{}/new/",
"it": "https://itch.io/search?q={}",
"tpb": "https://thepiratebay.org/search/{}/0/7/0",
"gi": "https://duckduckgo.com/?q={}&iar=images",
"p": "https://www.protondb.com/search?q={}",
"a": "https://www.amazon.co.uk/s/?url=search-alias&field-keywords={}"}
c.completion.open_categories = ["quickmarks", "bookmarks", "history"]
# ads
c.content.host_blocking.enabled = True
c.content.host_blocking.lists.append("http://sbc.io/hosts/hosts")
c.content.host_blocking.whitelist = ["thepiratebay.org"]

# zoom

c.zoom.default = 100

# colours

def read_xresources(prefix):
    props = {}
    x = subprocess.run(['xrdb', '-query'], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split('\n')
    for line in filter(lambda l : l.startswith(prefix), lines):
        prop, _, value = line.partition(':\t')
        props[prop] = value
    return props

xresources = read_xresources('*')

c.colors.completion.fg = xresources['*.foreground']
c.colors.completion.even.bg = xresources['*.background']
c.colors.completion.odd.bg = xresources['*.background']
c.colors.completion.category.fg = xresources['*.foreground']
c.colors.completion.category.bg = xresources['*.background']
c.colors.completion.category.border.top = xresources['*.background']
c.colors.completion.item.selected.fg = c.colors.completion.category.fg
c.colors.completion.item.selected.bg = xresources['*.color13']
c.colors.completion.item.selected.border.top = c.colors.completion.item.selected.bg
c.colors.completion.item.selected.border.bottom = xresources['*.background']
c.colors.completion.match.fg = xresources['*.color14']
c.colors.completion.scrollbar.bg = xresources['*.color0']
c.colors.completion.scrollbar.fg = xresources['*.color8']
c.colors.completion.category.border.bottom = xresources['*.background']
c.colors.completion.category.border.top = xresources['*.background']
c.colors.statusbar.command.fg = xresources['*.foreground']
c.colors.statusbar.command.bg = xresources['*.background']
c.colors.statusbar.insert.bg = xresources['*.color2']
c.colors.statusbar.caret.bg = xresources['*.color4']
c.colors.statusbar.progress.bg = xresources['*.foreground']
c.colors.statusbar.url.success.http.fg = xresources['*.foreground']
c.colors.statusbar.url.success.https.fg = xresources['*.color10']
c.colors.statusbar.url.error.fg = c.colors.completion.fg
c.colors.statusbar.url.warn.fg = c.colors.completion.fg
c.colors.statusbar.url.hover.fg = xresources['*.color14']
c.colors.tabs.odd.fg = xresources['*.foreground']
c.colors.tabs.odd.bg = "#555555"
c.colors.tabs.even.fg = c.colors.tabs.odd.fg
c.colors.tabs.even.bg = c.colors.tabs.odd.bg
c.colors.tabs.selected.odd.bg = xresources['*.color7']
c.colors.tabs.selected.odd.fg = xresources['*.background']
c.colors.tabs.selected.even.fg = c.colors.tabs.selected.odd.fg
c.colors.tabs.selected.even.bg = c.colors.tabs.selected.odd.bg
c.colors.tabs.bar.bg = '#292929'
c.hints.border = "1px solid transparent"
c.colors.hints.fg = xresources['*.background']
c.colors.hints.bg = xresources['*.color11']
c.colors.hints.match.fg = xresources['*.color2']
c.colors.downloads.bar.bg = xresources['*.background']
c.colors.downloads.start.fg = xresources['*.foreground']
c.colors.downloads.system.fg = "none"
c.colors.downloads.system.fg = "none"
c.colors.downloads.error.fg = xresources['*.foreground']
c.colors.downloads.error.bg = xresources['*.color13']
c.colors.webpage.bg = xresources['*.foreground']
c.colors.messages.error.fg = xresources['*.foreground']
c.colors.messages.error.bg = xresources['*.color5']
c.colors.messages.error.border = c.colors.messages.error.bg
c.colors.messages.warning.fg = xresources['*.foreground']
c.colors.messages.warning.bg = xresources['*.color4']
c.colors.messages.warning.border = c.colors.messages.warning.bg
c.colors.messages.info.fg = xresources['*.foreground']
c.colors.messages.info.bg = xresources['*.background']
c.colors.messages.info.border = c.colors.messages.info.bg
c.colors.prompts.fg = xresources['*.foreground']
c.colors.prompts.bg = xresources['*.color4']
c.colors.prompts.selected.bg = xresources['*.color12']

# fonts

c.fonts.monospace = "Fira Code"
c.fonts.web.family.fixed = c.fonts.monospace
c.fonts.web.family.sans_serif = "Noto Sans"
c.fonts.web.family.serif = c.fonts.web.family.sans_serif
c.fonts.web.family.standard = c.fonts.web.family.sans_serif


# keys

config.bind('<Ctrl-Shift-m>', 'spawn --detach mpv --force-window yes {url}')
# config.bind('<Ctrl-Shift-m>', 'spawn --detach mpv --force-window yes --ytdl-format=best[height=360] {url}')
config.bind('<Ctrl-Shift-p>', 'spawn --userscript password_fill')
config.bind('z', 'download-open')
config.bind('xx', 'set tabs.show always;; later 50000 set tabs.show never')
config.bind('xb', 'config-cycle statusbar.hide')
config.bind('tg', 'tab-give')
config.unbind('q')
config.unbind('<Ctrl-v>')
config.bind('<Ctrl-y>', 'hint links spawn --detach mpv --force-window yes --ytdl-format=best[height=360] {hint-url}')

# Dealing with login forms
config.bind('<,><l>', 'spawn --userscript qute-pass')
config.bind('<,><u><l>', 'spawn --userscript qute-pass --username-only')
config.bind('<,><p><l>', 'spawn --userscript qute-pass --password-only')
config.bind('<,><o><l>', 'spawn --userscript qute-pass --otp-only')