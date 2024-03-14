##############################################################################
####### Find Domain Name From DNS Pointer (PTR) Records Using IP Address
"""
Task :
Write a function that takes an IP address and returns the domain name using PTR DNS records.

Example
get_domain("8.8.8.8") ➞ "dns.google"
get_domain("8.8.4.4") ➞ "dns.google"
"""
# 1st method
import socket

def get_domain(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except socket.herror:
        return None

# OR 
import socket
def get_domain(ip_address):
	return socket.gethostbyaddr(ip_address)[0]

# 2nd method
from socket import getfqdn as get_domain

##############################################################################
# Find Domain Name From DNS Pointer (PTR) Records Using IP Address
"""
C*ns*r*d Str*ngs
Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily,
I've been able to find the vowels that were removed.
Given a censored string and a string of the censored vowels, return the original uncensored string.
Example :-
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
uncensor("abcd", "") ➞ "abcd"
uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
"""

