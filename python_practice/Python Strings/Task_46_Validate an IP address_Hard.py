"""You are given a string s in the form of an IPv4 Address. Your task is to validate an IPv4 Address, if it is valid return true otherwise return false.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., "172.16.254.1"

A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255. Thus, we can write the generalized form of an IPv4 address as (0-255).(0-255).(0-255).(0-255)"""
import re

class Solution:
    def isValidIPv4(self, s):
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        
        if re.match(pattern, s):
            parts = s.split(".")
            for p in parts:
                if not 0 <= int(p) <= 255:
                    return False
            return True
        return False


obj = Solution()
print(obj.isValidIPv4("172.16.254.1"))   
print(obj.isValidIPv4("256.16.254.1"))   