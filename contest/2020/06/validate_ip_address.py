class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            valid4 = { str(i) for i in range(256) }
            if all([group in valid4 for group in IP.split('.')]):
                return 'IPv4'
        if IP.count(':') == 7:
            valid6 = { hex(i).replace('0x', '') for i in range(16) }
            if all([0 < len(group) <= 4 and all([digit.lower() in valid6 for digit in group]) for group in IP.split(':')]):
                return 'IPv6'
        return 'Neither'
