# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://shadowmere.xyz/api/b64sub/",
    "https://zood.link/Tr_hamedp71",
    "https://raw.githubusercontent.com/iPsycho1/ss-config-updater/refs/heads/main/configs.txt",
    "https://raw.githubusercontent.com/iPsycho1/Subscription/refs/heads/main/iPsycho_Location",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_BASE64.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_RAW.txt",
    "https://fs.v2rayse.com/share/20250417/kn4eyffwk0.json#kn4eyffwk0",
    "https://zaya.link/T_hamedp71",
    "https://xb.inekokkk.com/amei/0c230a6f6a95c9a9d3cdada708c9b1cb",
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
