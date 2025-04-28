# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://raw.githubusercontent.com/4n0nymou3/ss-config-updater/refs/heads/main/configs.txt",
    "https://t.me/s/Suevpnx",
    "https://panel.maviks.eu/sub/NTYyMjc2NDA5LDE3NDU2NjI4MzEduSSa0rsbQ",
    "https://fs.v2rayse.com/share/20250417/kn4eyffwk0.json#kn4eyffwk0",
    "https://raw.githubusercontent.com/IranRamona/singbox/refs/heads/main/sub/wearestand.json",
    "https://raw.githubusercontent.com/iPsycho1/Subscription/refs/heads/main/iPsycho_Fragment",
    "https://raw.githubusercontent.com/IranianCypherpunks/Xray/main/Sub#𝐈𝐑𝐂𝐏",
    "https://raw.githubusercontent.com/iPsycho1/ss-config-updater/refs/heads/main/configs.txt",
    "https://shadowmere.xyz/api/b64sub/#@redfree8",
    "https://raw.githubusercontent.com/NiREvil/vless/main/sub/SSTime",
    "https://panel.maviks.eu/sub/NjE3Mzg1MTE4MywxNzQ1NjYzODY5ac1o7kfeLv",
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = False

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 100

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": True,
    "ss://": True,
    "trojan://": True,
    "tuic://": True,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 7
